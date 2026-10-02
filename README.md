# SASD Graphics Toolkit

[![CMake](https://github.com/Robin-Goerlach/SASD-Graphics-Toolkit/actions/workflows/cmake.yml/badge.svg)](https://github.com/Robin-Goerlach/SASD-Graphics-Toolkit/actions/workflows/cmake.yml)
![Status](https://img.shields.io/badge/status-multilanguage%20foundation-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A reusable 2D graphics and visualization foundation for SASD projects.
**English is the default. [Deutsch](README.de.md).**

![Concept preview — not an application screenshot](assets/screenshots/sasd-graphics-toolkit-preview.svg)

## Scope
Scenes, styles, visual coordinates, renderer adapters, boards/grids and small charts.
SVG is the first planned renderer. Game rules/AI, numerical algorithms and UI-framework
core logic remain in their own projects. The core stays UI-framework independent.

## Two independent language dimensions
C++20/CMake is the first implementation direction. C#/.NET is a planned peer,
not an obligatory C++ wrapper. Later platform trees are additive.
English/German documentation is independent from implementation language.
Shared behavior lives in `spec/`; APIs remain idiomatic to each platform.
The layout follows [SASD Math Toolkit](https://github.com/Robin-Goerlach/SASD-Math-Toolkit).

## Repository layout
| Path | Purpose |
|---|---|
| `src/cpp/` | first C++20 implementation scaffold |
| `src/dotnet/` | planned C#/.NET peer implementation |
| `tests/cpp/`, `tests/dotnet/` | platform-specific tests |
| `samples/cpp/`, `samples/dotnet/` | platform-specific examples |
| `spec/` | shared contracts and reference data |
| `docs/en/`, `docs/de/` | human-language documentation |
| `resources/i18n/` | future localized message catalogs |
| `assets/` | shared images and media |

Public C++ headers will live in `src/cpp/include/sasd/graphics/`.
Root `include/` and former numbered documentation paths retain migration pointers.
There are no translated copies of library source code.

## Current status
**Repository foundation only.** No graphics library, renderer, executable sample,
.NET project or package is implemented. CMake and CTest currently configure the
C++ scaffold and validate repository/documentation contracts.
The four shared affine reference cases are data; no C++/.NET runner executes them yet.
Empty English/German text catalogs do not imply working runtime localization.
See [language support](docs/en/070_Language_Support.md).

## Configure, check and build
Requirements: CMake >= 3.22, a C++20-capable compiler and Python >= 3.10 when checks are enabled.
.NET is not required for the C++ scaffold.

```bash
python3 tools/check_repository.py
cmake -S . -B build -DSASD_GRAPHICS_BUILD_TESTS=ON
cmake --build build --config Release
ctest --test-dir build --output-on-failure -C Release
```

Windows: use `python` if your Python installation does not expose `python3`.
Python may be omitted with `-DSASD_GRAPHICS_BUILD_TESTS=OFF`.
There are no library/sample build targets yet.

## Documentation
- [English index](docs/en/README.md) / [Deutscher Index](docs/de/README.md)
- [Architecture and decisions](docs/en/020_Architecture.md)
- [Multi-language workflow](docs/en/050_Multilanguage_Development.md)
- [Shared contracts](docs/en/060_Contracts.md)
- [Roadmap](docs/en/030_Roadmap.md)
- [Math/GameWorks/UI integration](docs/en/040_Integration_GameWorks_Numerics.md)
- [Historical GameWorks discussion context](docs/en/090_Conversation_Context.md)
- [Development rules](AGENTS.md) / [Arbeitsregeln](AGENTS.de.md)
- [Contributing](CONTRIBUTING.md) / [Beiträge](CONTRIBUTING.de.md)

Math owns reusable mathematics; Graphics visualizes. A small Math geometry dependency
is proposed, but no package or interoperability boundary has been selected.
The Math core must stay independent of Graphics.
Historical discussion context is non-normative; current architecture decisions take precedence.

## First planned demo
A small 19 × 19 Go-Moku board exported as SVG, with stones, last-move marker,
labels and coordinate mapping. Game rules remain outside Graphics.

## License
MIT: [LICENSE](LICENSE). [German reading aid](LICENSE.de.md);
the English LICENSE is authoritative.
