# Contributing
[Deutsch](CONTRIBUTING.de.md).

Keep changes small, documented and driven by actual consumers.
Follow [AGENTS.md](AGENTS.md), the [architecture](docs/en/020_Architecture.md)
and the [multi-language workflow](docs/en/050_Multilanguage_Development.md).
Use `src/<platform>/`, `tests/<platform>/`, `samples/<platform>/`.
Shared contracts belong in `spec/`; runtime text catalogs in `resources/i18n/`.
English is default; update the mapped German document and its reviewed source hash.
Record supported capabilities honestly; prepared directories are not implementations.

The core covers scene/style/rendering/visual coordinates and boards/charts.
Keep game rules, AI, numerical algorithms and UI-framework logic outside Graphics.
Resolve Math ownership before adding generic math primitives.

Run:
```bash
python3 tools/check_repository.py
cmake -S . -B build
cmake --build build --config Release
ctest --test-dir build --output-on-failure -C Release
```
Requirements: CMake >= 3.22, C++20-capable compiler, Python >= 3.10.
On Windows use `python` if needed. Current CTest validates repository consistency;
add meaningful implementation tests when adding code.
