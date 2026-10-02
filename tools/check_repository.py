#!/usr/bin/env python3
"""Validate repository/data contracts, not a graphics library implementation."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def require(condition, message):
    if not condition:
        raise ValueError(message)


def unique_object(pairs):
    """Reject duplicate JSON keys instead of silently accepting the last value."""
    result = {}
    for key, value in pairs:
        require(key not in result, f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def local_path(root, name):
    require(isinstance(name, str) and bool(name), "Expected a non-empty path")
    path = (root / name).resolve()
    require(path.is_relative_to(root), f"Path escapes repository: {name}")
    require(path.exists(), f"Missing path: {name}")
    return path


def unique_ids(items, label):
    ids = [item["id"] for item in items]
    require(len(ids) == len(set(ids)), f"Duplicate {label} ID")
    return ids


def finite_numbers(values, count, label):
    require(isinstance(values, list) and len(values) == count, f"Invalid {label} size")
    require(all(type(v) in (int, float) and math.isfinite(v) for v in values),
            f"Non-finite/non-numeric {label}")


def check_links(root):
    """Check file targets; external URLs and heading anchors are outside this gate."""
    ignored = {".git", "build", "Build", "out", "artifacts", "bin", "obj",
               "CMakeFiles", "__pycache__"}
    count = 0
    for directory, dirs, names in os.walk(root):
        dirs[:] = [d for d in dirs if d not in ignored and not d.startswith("build-")]
        for name in names:
            if not name.endswith(".md"):
                continue
            path = Path(directory) / name
            content = path.read_text(encoding="utf-8")
            fence = chr(96) * 3
            content = re.sub(fence + r".*?" + fence, "", content, flags=re.S)
            for target in re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", content):
                target = target.strip().split(' "', 1)[0].strip("<>")
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                resolved = (path.parent / unquote(parsed.path)).resolve()
                require(resolved.is_relative_to(root),
                        f"{path.relative_to(root)}: link escapes root")
                require(resolved.exists(),
                        f"{path.relative_to(root)}: broken link {target}")
                count += 1
    return count


def validate(root, print_hashes=False):
    project = read_json(root / "spec/project.json")
    require(project["schema_version"] == 1, "Unsupported project schema")
    platforms, locales = project["platforms"], project["locales"]
    unique_ids(platforms, "platform")
    locale_ids = unique_ids(locales, "locale")
    default = project["default_documentation_locale"]
    require(default == "en" and default in locale_ids, "English must be the registered default")
    catalogs = {}
    for platform in platforms:
        require(platform["kind"] in {"peer-implementation", "binding"}, "Invalid platform kind")
        require(platform["status"] in {"planned", "scaffold", "implemented"}, "Invalid platform status")
        for key, prefix in (("source", "src"), ("tests", "tests"), ("samples", "samples")):
            require(platform[key] == f"{prefix}/{platform['id']}",
                    f"Inconsistent platform path: {platform[key]}")
            require(local_path(root, platform[key]).is_dir(), "Platform path must be a directory")
        require(isinstance(platform["implemented_capabilities"], list), "Capabilities must be a list")
        if platform["status"] != "implemented":
            require(not platform["implemented_capabilities"],
                    f"Unimplemented platform claims capabilities: {platform['id']}")
    for locale in locales:
        require(locale["documentation"] == f"docs/{locale['id']}", "Inconsistent locale path")
        require(local_path(root, locale["documentation"]).is_dir(), "Docs path must be a directory")
        require(locale["catalog"] == f"resources/i18n/{locale['id']}.json", "Inconsistent catalog path")
        require(locale["runtime_status"] in {"not-implemented", "implemented"}, "Invalid runtime status")
        catalog = read_json(local_path(root, locale["catalog"]))
        require(isinstance(catalog, dict) and all(isinstance(v, str) for v in catalog.values()),
                f"Catalog must map keys to strings: {locale['id']}")
        catalogs[locale["id"]] = catalog
    for locale, catalog in catalogs.items():
        require(set(catalog) == set(catalogs[default]), f"Catalog key mismatch: {locale}")

    contracts = read_json(root / "spec/contracts.json")
    require(contracts["schema_version"] == 1 and contracts["status"] == "draft",
            "Review validator before promoting draft contract schema")
    contract_ids = set(unique_ids(contracts["contracts"], "contract"))
    for platform in platforms:
        require(set(platform["implemented_capabilities"]) <= contract_ids, "Unknown capability")
    vectors = read_json(root / "spec/test-vectors/affine2d.json")
    require(vectors["schema_version"] == 1, "Unsupported vector schema")
    require(vectors["contract_id"] == "GFX-COORD-001" and vectors["contract_id"] in contract_ids,
            "Wrong affine vector contract")
    require(vectors["status"] == "reference-data-only", "Reference data misrepresented")
    tolerances = [vectors["abs_tolerance"], vectors["rel_tolerance"]]
    finite_numbers(tolerances, 2, "tolerances")
    require(all(t >= 0 for t in tolerances), "Negative tolerance")
    require(vectors["cases"], "Missing affine reference cases")
    unique_ids(vectors["cases"], "reference case")
    for case in vectors["cases"]:
        finite_numbers(case["matrix"], 6, "matrix")
        finite_numbers(case["point"], 2, "point")
        finite_numbers(case["expected"], 2, "expected")
        a, b, c, d, tx, ty = case["matrix"]
        x, y = case["point"]
        reference = [a*x + c*y + tx, b*x + d*y + ty]
        for actual, expected in zip(reference, case["expected"]):
            limit = max(tolerances[0], tolerances[1] * abs(expected))
            require(math.isfinite(actual) and abs(actual-expected) <= limit,
                    f"Inconsistent reference data: {case['id']}")

    documents = read_json(root / "spec/documentation.json")
    require(documents["schema_version"] == 1, "Unsupported document schema")
    unique_ids(documents["documents"], "document")
    mapped_paths, hashes, warnings = set(), [], []
    for doc in documents["documents"]:
        require(doc["source_locale"] == default, f"Wrong source locale: {doc['id']}")
        source = local_path(root, doc["source"])
        require(source.is_file(), f"Document source must be a file: {doc['id']}")
        # Canonical UTF-8/LF hashing keeps source revisions portable to Windows
        # checkouts that use CRLF. Content changes still invalidate the review.
        source_hash = hashlib.sha256(source.read_text(encoding="utf-8").encode("utf-8")).hexdigest()
        hashes.append(f"{doc['id']} {source_hash}")
        require(doc["source"] not in mapped_paths, "Duplicate document path")
        mapped_paths.add(doc["source"])
        require(set(doc["translations"]) == set(locale_ids)-{default},
                f"Missing locale mapping: {doc['id']}")
        for locale, translation in doc["translations"].items():
            if translation["status"] == "missing":
                require(bool(translation.get("reason")), "Missing translation needs a reason")
                warnings.append(f"{doc['id']}: missing {locale} translation")
                continue
            require(translation["status"] == "reviewed", "Unknown translation status")
            require(local_path(root, translation["path"]).is_file(), "Translation must be a file")
            require(translation["path"] not in mapped_paths, "Duplicate translation path")
            mapped_paths.add(translation["path"])
            if not print_hashes:
                require(translation["reviewed_source_sha256"] == source_hash,
                        f"Stale source revision: {doc['id']}/{locale}; review both editions "
                        "and update documentation.json")
    # A new substantive document must not bypass registration/translation tracking.
    for locale in locale_ids:
        for path in (root / f"docs/{locale}").rglob("*.md"):
            require(path.relative_to(root).as_posix() in mapped_paths,
                    f"Unregistered document: {path.relative_to(root)}")
    links = check_links(root)
    if print_hashes:
        print("\n".join(hashes))
    else:
        print(f"OK: {len(platforms)} platform trees, {len(locales)} locales, "
              f"{len(documents['documents'])} document pairs, {links} local links, "
              f"{len(vectors['cases'])} affine reference data cases")
        print("Repository/data validation only; no graphics implementation tests.")
    for warning in warnings:
        print(f"NOTE: {warning}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--print-source-hashes", action="store_true",
                        help="Print source hashes for manual recording after translation review")
    args = parser.parse_args()
    try:
        validate(args.root.resolve(), args.print_source_hashes)
    except (ValueError, KeyError, TypeError, OSError, OverflowError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
