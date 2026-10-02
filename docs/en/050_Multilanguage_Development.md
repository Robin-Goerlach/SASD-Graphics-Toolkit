# Multi-language development
Document ID: GFX-DOC-LANGUAGES.

## Independent dimensions
Implementation platforms (`cpp`, `dotnet`, later others) and human locales
(`en`, `de`, later BCP 47 tags) are independent.
The repository follows the Math Toolkit structure. Extend the registry in
[project.json](../../spec/project.json), create the needed platform paths,
and add real build/test jobs only when code exists.

## Shared behavior, idiomatic APIs
English contract IDs and machine-readable data are stable across platforms.
Use natural C++ and .NET naming, ownership and error mechanisms.
Map these mechanisms to the same documented semantic outcomes.
A peer implementation owns its code; a binding delegates to another implementation.
Document that distinction and supported capabilities before publication.

## Documentation workflow
English is the normative default; German companions must convey the same decisions.
Work may be drafted in German, then reconcile both editions before completion.
Root entry files retain `.de.md`; substantive documents use `docs/en/` and `docs/de/`.
Stable document IDs map editions in [documentation.json](../../spec/documentation.json).
Localized filenames may differ; never infer a pair from filename similarity alone.
Old documentation paths contain redirects, not independently edited prose.

For a content change:
1. Edit the English document and its German edition.
2. Review German meaning against the revised English source.
3. Run `python3 tools/check_repository.py --print-source-hashes` from repository root.
4. Record the reviewed English SHA-256 in the corresponding translation entry.
5. Run `python3 tools/check_repository.py`.

The source hash detects an outdated source revision; it cannot judge translation quality.
Paths and links are checked, not external-site availability.
Missing translations are explicit; do not silently label fallback text as translated.
To add a locale, add its document/resource mappings and reviewed hashes.

## Comments and terminology
API identifiers and primary code comments are English.
Use explanatory C++ `//` or `/** */` and C# `///` comments where intent,
invariants and ownership need explanation.
German developer explanations belong in the German documents.
Keep the English/German glossary in [contracts](060_Contracts.md) aligned.

## Runtime localization — prepared, not implemented
[resources/i18n](../../resources/i18n/README.md) holds UTF-8 JSON text catalogs.
The current catalogs are empty; no language switching or fallback runtime exists.
Later demos resolve stable message keys, explicitly select locale and fall back to English.
The graphics core must not change behavior based on process-wide language settings.
User-provided titles/legends are preserved, not automatically translated.
Technical SVG numbers use invariant decimal points; visible labels may be localized.
Unicode/XML escaping is required; complex-script shaping, fonts and bidirectional
layout need explicit backend capabilities rather than a blanket language-support claim.
