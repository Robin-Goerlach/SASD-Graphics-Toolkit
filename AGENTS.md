# Development rules
[Deutsch](AGENTS.de.md).

## Architecture
Follow the Math Toolkit layout: `src/<platform>`, `tests/<platform>`,
`samples/<platform>`, shared `spec/` and `docs/<locale>/`.
Use `cpp` and `dotnet` consistently, including examples; do not mix in `csharp`.
C++20 is first; C#/.NET is a planned peer, not an obligatory wrapper.
Additional platforms/locales must be registered in [spec/project.json](spec/project.json).
Root AGENTS.md is authoritative; its German companion must convey the same rules.

## Scope and dependencies
Keep the core UI-independent. No game rules, AI or UI-framework core logic.
Before implementing generic math primitives, resolve ownership and the small Math
integration described in [ADR-GFX-003](docs/en/020_Architecture.md).
Never make Math core depend on Graphics. No Math dependency is currently configured.
Read [shared contracts](docs/en/060_Contracts.md) before adding public APIs.
Do not add a runtime/binding/large abstraction without an actual consumer need.

## Code and tests
Use idiomatic platform APIs, English identifiers and explanatory English comments:
C++ `//`/`/** */`, C# `///` as appropriate.
Explain intent, invariants and ownership, not just the statement being executed.
Keep IO/UI in samples/adapters. Tests must exercise real public behavior.
Future runners consume shared vectors with their explicit tolerances.
Prefer geometry invariants and SVG structure/coordinates over pixel-only checks.

## Documentation
English default; German companion. Substantive docs use `docs/en/`, `docs/de/`.
Root companions retain `.de.md`. Document IDs and translation mappings live in
`spec/documentation.json`. Update both editions and reviewed source hashes after
semantic review; [workflow](docs/en/050_Multilanguage_Development.md).
Old documentation paths are redirects, not second editorial sources.
Distinguish planned, scaffold and implemented. Never claim an empty build is a library test.

## Required checks
```bash
python3 tools/check_repository.py
cmake -S . -B build -DSASD_GRAPHICS_BUILD_TESTS=ON
cmake --build build --config Release
ctest --test-dir build --output-on-failure -C Release
```
Requirements: Python >= 3.10, CMake >= 3.22, C++20-capable compiler.
On Windows `python` may replace `python3`. Build each affected platform when real code exists.
Current CTest checks repository consistency only. No numerical/renderer runner exists.

## Implementation order
Resolve Math/geometry boundary, coordinates, scene/styles, SVG, then Go-Moku sample.
Second-platform scope follows a real consumer; do not create dummy package projects.
