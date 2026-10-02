# Language-neutral specification
This directory follows the SASD Math Toolkit contract-layer convention.
English technical descriptions are authoritative; localized explanations live in
[docs/en/060_Contracts.md](../docs/en/060_Contracts.md) and
[docs/de/060_Contracts.md](../docs/de/060_Contracts.md).

- [project.json](project.json): registered platforms/locales and honest support status.
- [documentation.json](documentation.json): document identities, translation paths and reviewed source revisions.
- [contracts.json](contracts.json): draft requirements with stable contract IDs.
- [test-vectors/affine2d.json](test-vectors/affine2d.json): shared affine reference data.

No production implementation or cross-language runner consumes these contracts yet.
The repository validator checks structural integrity, links and reviewed source hashes.
It is not a numerical library acceptance test.
