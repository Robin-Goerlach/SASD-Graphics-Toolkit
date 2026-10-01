# Integration with GameWorks Lab and Numerics

This document explains how **SASD Graphics Toolkit** should interact with related SASD projects.

## Role of the Graphics Toolkit

The Graphics Toolkit is responsible for visualization infrastructure:

- drawing models,
- geometry primitives,
- coordinate mapping,
- scene and layer structures,
- renderers,
- board and chart visualization helpers.

It should not own domain logic.

## GameWorks Lab

**SASD GameWorks Lab** should own game rules, game states, legal moves, evaluation, search, and AI logic.

The Graphics Toolkit can provide:

- generic grids,
- Go-Moku board rendering,
- chess-board rendering,
- coordinate labels,
- last-move markers,
- hit testing from device position to board coordinate,
- search-tree or evaluation diagrams later.

Rule of thumb:

> GameWorks decides what a position means. Graphics decides how it is drawn.

## Numerics / Math Toolkit

**SASD Numerics / Math Toolkit** should own numerical algorithms, statistics, functions, interpolation, optimization, and mathematical models.

The Graphics Toolkit can provide:

- axes,
- plot areas,
- line and scatter series,
- scaling and coordinate mapping,
- legends,
- exportable SVG diagrams.

Rule of thumb:

> Numerics computes values. Graphics presents values.

## UI Toolkit / UI Platform

**SASD UI Toolkit** and **SASD UI Platform** may later consume the graphics core for reusable drawing primitives, preview components, or rendering adapters.

The Graphics Toolkit should not depend on UI projects in its core. UI projects may depend on the Graphics Toolkit, not the other way around.

## Dependency Direction

Preferred direction:

```text
GameWorks Lab  ---> Graphics Toolkit
Numerics       ---> Graphics Toolkit
UI Toolkit     ---> Graphics Toolkit
```

Avoid:

```text
Graphics Toolkit ---> GameWorks Lab
Graphics Toolkit ---> Numerics
Graphics Toolkit ---> UI Toolkit core logic
```

## First Shared Scenario

The first practical integration scenario should be a Go-Moku board:

1. GameWorks produces a board state.
2. Graphics converts the board state into a scene.
3. The SVG renderer writes the scene to an SVG file.
4. Tests verify board coordinates and SVG structure.
