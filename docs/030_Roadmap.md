# Roadmap

This roadmap describes a sensible development order for **SASD Graphics Toolkit**. It is intentionally staged so that visible results appear early without overbuilding the architecture.

## M0 – Repository Baseline

Goal: make the public repository understandable and ready for development.

Result:

- English README as default.
- German companion documentation.
- SVG preview image.
- Documentation directory.
- Architecture overview.
- Feature catalog.
- AGENTS.md.
- CMake baseline.
- MIT license confirmed.

## M1 – Core Geometry

Goal: create the foundation for all later graphics work.

Scope:

- `point2d`
- `size2d`
- `vector2d`
- `rect2d`
- `line_segment2d`
- `bounds2d`

Acceptance criteria:

- Unit tests for all public types.
- No dependency on UI frameworks.
- Public types have clear comments and examples.

## M2 – Coordinate Mapping

Goal: convert between model, world, and output coordinates.

Scope:

- viewport,
- world-to-device mapping,
- scaling,
- translation,
- optional y-axis inversion,
- basic bounds clipping.

## M3 – Scene Model and Styles

Goal: describe drawings as testable models.

Scope:

- scene,
- layer,
- shape primitives,
- stroke/fill/text styles,
- simple z-order.

## M4 – SVG Renderer

Goal: produce visible output from the scene model.

Scope:

- lines,
- rectangles,
- circles,
- text,
- simple paths/polylines,
- viewBox support.

## M5 – Board Renderer

Goal: prepare visualization for GameWorks Lab.

Scope:

- generic grid,
- Go-Moku board,
- chess-board baseline,
- coordinate labels,
- markers/stones/placeholders,
- hit testing.

## M6 – Chart Basics

Goal: provide first useful visualization for Numerics/Math Toolkit.

Scope:

- axes,
- scaling,
- polyline series,
- scatter series,
- simple legend,
- function-plot demo.

## M7 – Demo Application

Goal: create a practical visual testbed.

Scope:

- small demo app or command-line demo generator,
- board preview,
- chart preview,
- SVG export,
- coordinate/hit-test diagnostics.

## M8 – Stabilization and First Pre-Release

Goal: prepare a first usable preview version.

Scope:

- API review,
- documentation cleanup,
- example cleanup,
- CI verification,
- release notes.

## Priority Rule

When in doubt, prefer a small working demo plus tests over a large abstract framework.
