# SASD Graphics Toolkit

[![CMake](https://github.com/Robin-Goerlach/SASD-Graphics-Toolkit/actions/workflows/cmake.yml/badge.svg)](https://github.com/Robin-Goerlach/SASD-Graphics-Toolkit/actions/workflows/cmake.yml)
![Status](https://img.shields.io/badge/status-concept%20baseline-blue)
![Language](https://img.shields.io/badge/language-C%2B%2B20-informational)
![License](https://img.shields.io/badge/license-MIT-green)

> Modern C++ graphics, visualization, and drawing foundation for SASD projects.

**Language:** English is the default documentation language. A German version is available in [README.de.md](README.de.md).

![SASD Graphics Toolkit Preview](assets/screenshots/sasd-graphics-toolkit-preview.svg)

## Vision

**SASD Graphics Toolkit** is intended to become a small, clean, and extensible C++20 library for reusable 2D graphics building blocks. It is not planned as a full game engine, a complete GUI framework, or a replacement for Qt, GTK, wxWidgets, Skia, or Cairo.

The toolkit should provide the graphics foundation for several SASD projects:

- **SASD GameWorks Lab:** board rendering, card layouts, search-tree views, move-analysis diagrams, score timelines.
- **SASD Numerics / Math Toolkit:** function plots, axes, grids, diagrams, and numerical visualization.
- **SASD UI Toolkit / UI Platform:** reusable drawing models, geometry, themes, grids, and later renderer adapters.
- **Learning and research projects:** compact examples for geometry, transformations, rendering, and algorithmic visualization.

## Core Idea

The project separates the following concerns:

```text
Graphics model      -> what should be drawn?
Layout/coordinates  -> where and at which scale?
Renderer backend    -> how is it emitted or displayed?
Application logic   -> why is it drawn?
```

This should make it possible to render the same conceptual scene to different targets later, for example SVG, bitmap images, Win32/GDI+, Direct2D, Skia, Cairo, HTML Canvas, or an experimental terminal-oriented backend.

## Planned Feature Areas

| Area | Planned scope |
|---|---|
| **Core Geometry** | points, vectors, sizes, rectangles, bounds, lines, circles, polygons |
| **Coordinate Mapping** | world coordinates, device coordinates, viewports, transforms |
| **Scene Model** | scenes, layers, shapes, text, styles, stable IDs |
| **Rendering** | SVG first, bitmap and native backends later |
| **Boards & Grids** | Go-Moku board, chess board, generic grids, hit testing |
| **Charts** | axes, polylines, scatter plots, simple legends |
| **Demos** | small examples instead of one large demo monolith |
| **Tests** | geometry, mapping, scene modeling, SVG output, board mapping |

## Project Boundaries

The toolkit should not contain game rules, chess logic, Go-Moku AI, Bridge bidding, or numerical algorithms. Those belong into separate projects. This repository should stay focused on visualization and rendering infrastructure.

```text
SASD.GameWorksLab        -> game rules, AI, game states
SASD.Numerics.Core       -> mathematics, statistics, numerical methods
SASD.Graphics.Toolkit    -> drawing models, coordinates, rendering, visualization
SASD.UI.Toolkit          -> interaction concepts and UI widgets
```

## Repository Layout

```text
include/    public C++ headers
src/        implementation files
tests/      future unit and regression tests
docs/       English documentation plus German companion documents
assets/     screenshots, diagrams, and visual material
```

## Suggested First Demo

A **Go-Moku board renderer** is the recommended first demo because it is small enough for a fast start and useful for the later GameWorks project:

- 19 × 19 grid
- stones as simple circles
- last move marker
- A–S / 1–19 labels
- mapping from mouse/device position to board coordinate
- SVG export

## Documentation

| English document | German companion |
|---|---|
| [docs/README.md](docs/README.md) | [docs/README.de.md](docs/README.de.md) |
| [docs/000_Project_Overview.md](docs/000_Project_Overview.md) | [docs/000_Project_Overview.de.md](docs/000_Project_Overview.de.md) |
| [docs/010_Feature_Catalog.md](docs/010_Feature_Catalog.md) | [docs/010_Feature_Catalog.de.md](docs/010_Feature_Catalog.de.md) |
| [docs/020_Architecture.md](docs/020_Architecture.md) | [docs/020_Architecture.de.md](docs/020_Architecture.de.md) |
| [docs/030_Roadmap.md](docs/030_Roadmap.md) | [docs/030_Roadmap.de.md](docs/030_Roadmap.de.md) |
| [docs/040_Integration_GameWorks_Numerics.md](docs/040_Integration_GameWorks_Numerics.md) | [docs/040_Integration_GameWorks_Numerics.de.md](docs/040_Integration_GameWorks_Numerics.de.md) |
| [docs/090_Conversation_Context.md](docs/090_Conversation_Context.md) | [docs/090_Conversation_Context.de.md](docs/090_Conversation_Context.de.md) |
| [AGENTS.md](AGENTS.md) | [AGENTS.de.md](AGENTS.de.md) |
| [CONTRIBUTING.md](CONTRIBUTING.md) | [CONTRIBUTING.de.md](CONTRIBUTING.de.md) |

The `090_Conversation_Context*` documents preserve useful background from the broader GameWorks discussion. They are deliberately non-normative; newer architecture documents, ADRs, and implemented code take precedence.

## Build Baseline

The repository is prepared as a C++20/CMake project:

```bash
cmake -S . -B build
cmake --build build
ctest --test-dir build
```

## Status

Current status: **concept baseline / repository foundation**.

The project does not yet provide a stable API or production-ready implementation.

## License

This repository is licensed under the **MIT License**. See [LICENSE](LICENSE). A non-authoritative German reading aid is available in [LICENSE.de.md](LICENSE.de.md); the English `LICENSE` file remains legally authoritative.

## Motto

> Do not just draw pixels. Draw models that can be understood, tested, and reused.