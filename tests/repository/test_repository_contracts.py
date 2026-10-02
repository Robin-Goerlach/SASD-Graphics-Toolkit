"""Exercise the repository gate with deliberately inconsistent temporary checkouts."""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]


class RepositoryGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "checkout"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(
            ".git", "build", "build-*", "__pycache__", "artifacts"))

    def run_gate(self):
        return subprocess.run(
            [sys.executable, str(self.root / "tools/check_repository.py"),
             "--root", str(self.root)], capture_output=True, text=True)

    def assert_rejected(self, message):
        result = self.run_gate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(message, result.stderr)

    def change_json(self, name, change):
        path = self.root / name
        value = json.loads(path.read_text(encoding="utf-8"))
        change(value)
        path.write_text(json.dumps(value), encoding="utf-8")

    def test_consistent_checkout_passes(self):
        result = self.run_gate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_changed_source_requires_translation_review(self):
        path = self.root / "docs/en/020_Architecture.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nNew decision.\n", encoding="utf-8")
        self.assert_rejected("Stale source revision")

    def test_crlf_source_checkout_preserves_reviewed_revision(self):
        mapping = json.loads((self.root / "spec/documentation.json").read_text(encoding="utf-8"))
        for document in mapping["documents"]:
            path = self.root / document["source"]
            path.write_bytes(path.read_bytes().replace(b"\r\n", b"\n").replace(b"\n", b"\r\n"))
        result = self.run_gate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_broken_local_link_is_rejected(self):
        path = self.root / "samples/cpp/README.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n[Missing](missing.md)\n", encoding="utf-8")
        self.assert_rejected("broken link")

    def test_catalog_key_drift_is_rejected(self):
        self.change_json("resources/i18n/de.json", lambda value: value.update({"extra": "Text"}))
        self.assert_rejected("Catalog key mismatch")

    def test_planned_platform_cannot_claim_implemented_capability(self):
        def change(value):
            value["platforms"][1]["implemented_capabilities"] = ["GFX-COORD-001"]
        self.change_json("spec/project.json", change)
        self.assert_rejected("Unimplemented platform claims capabilities")

    def test_inconsistent_reference_output_is_rejected(self):
        def change(value):
            value["cases"][0]["expected"][0] = 100
        self.change_json("spec/test-vectors/affine2d.json", change)
        self.assert_rejected("Inconsistent reference data")

    def test_unregistered_document_is_rejected(self):
        (self.root / "docs/en/unregistered.md").write_text("# Unregistered\n", encoding="utf-8")
        self.assert_rejected("Unregistered document")


if __name__ == "__main__":
    unittest.main()
