# Feature Catalog

This document collects the planned feature areas of **SASD Graphics Toolkit**. The list is ordered by dependency and practical implementation priority.

## P0 – Repository and Documentation Baseline

- English README as the default entry point.
- German companion README.
- Documentation directory.
- Architecture overview.
- Roadmap.
- AGENTS.md for AI-assisted development.
- MIT license information.

## P1 – Core Geometry

Foundation for all later modules:

- `point2d`
- `size2d`
- `vector2d`
- `rect2d`
- `line_segment2d`
- `circle2d`
- `polygon2d`
- `bounds2d`

Basic operations:

- distance calculation,
- bounds calculation,
- simple intersection and containment checks,
- rectangle normalization,
- mapping between world and output coordinates.

## P2 – Styling

Styles describe presentation, not domain logic:

- colors,
- stroke width,
- stroke style,
- fill style,
- text style,
- symbol style,
- themes.

The core should use its own simple style model and should not expose Win32, Qt, GTK, Skia, or Cairo types directly.

## P3 – Scene Model

The scene model describes what should be drawn:

- line,
- rectangle,
- circle/ellipse,
- polygon,
- path,
- text,
- layer,
- group,
- z-order,
- optional IDs for hit testing and debugging.

## P4 – SVG Renderer

SVG is the recommended first output format because it is text-based, easy to test, useful in Markdown, and independent of native UI frameworks.

Minimum scope:

- lines,
- rectangles,
- circles,
- simple paths,
- text,
- styles,
- viewBox,
- export to `.svg`.

## P5 – Boards and Grids

Planned board/grid functions:

- Go-Moku board, 19 × 19,
- chess board, 8 × 8,
- generic cell grid,
- card layout areas for later Bridge/card demos,
- cell labels,
- selected-cell or last-move highlighting,
- device position to board coordinate mapping,
- board coordinate to center-point mapping.

## P6 – Charts

Charts should start small:

- function plot,
- polyline plot,
- scatter plot,
- bar chart,
- simple axes,
- simple legend.

Later candidates:

- histogram,
- box plot,
- heatmap,
- search-tree visualization,
- Game-AI evaluation timeline.

## P7 – Renderer Backends

Possible later backends:

| Backend | Purpose |
|---|---|
| Bitmap | image export for documentation and tests |
| Win32/GDI+ | simple Windows demo backend |
| Direct2D | later higher-performance Windows backend |
| Skia | cross-platform 2D rendering |
| Cairo | cross-platform 2D rendering, especially useful on Linux |
| Terminal/Sixel | experimental terminal-oriented visualization |
| HTML Canvas | later web/documentation export |

## P8 – Demos

Demos should stay small and explain one concept each:

- `demo_gomoku_board`
- `demo_function_plot`
- `demo_transforms`
- `demo_chess_board`
- `demo_svg_export`

## P9 – Tests

Test areas:

- geometry,
- coordinate transformations,
- bounds,
- board mapping,
- SVG output,
- chart scaling.

Many tests should be model-based or text-based, for example by checking SVG elements, coordinates, and bounds instead of relying only on pixel comparisons.
