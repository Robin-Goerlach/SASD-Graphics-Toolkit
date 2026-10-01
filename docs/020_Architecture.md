# Architecture Overview

## Goal

The architecture of **SASD Graphics Toolkit** should keep domain visualization, geometry, styling, and concrete rendering separate.

The key rule is:

> The graphics core must not know whether a scene is rendered to SVG, bitmap, Win32, Direct2D, Skia, Cairo, or a future UI backend.

## Layer Model

```text
Application / Demo
    |
    v
Domain-specific Visualizers
    |
    v
Scene Model
    |
    v
Geometry + Coordinates + Styles
    |
    v
Renderer Backend
```

## Planned Modules

| Module | Responsibility |
|---|---|
| `sasd::graphics::geometry` | points, vectors, rectangles, bounds, lines, circles |
| `sasd::graphics::coordinates` | viewports, world-to-device mapping, transforms |
| `sasd::graphics::style` | colors, strokes, fills, text styles, themes |
| `sasd::graphics::scene` | layers, shapes, text, IDs, z-order |
| `sasd::graphics::rendering::svg` | SVG export |
| `sasd::graphics::boards` | grids, board coordinates, hit testing |
| `sasd::graphics::charts` | axes, series, simple plots |

## Core Principles

1. The core is UI-framework independent.
2. Renderers translate the scene model into concrete output.
3. Domain-specific visualizers live outside the renderer.
4. Tests should validate geometry and exported text where possible.
5. Demos drive API shape before the library becomes too abstract.

## First Backend: SVG

SVG is the preferred first backend because it is text-based, reviewable, easy to test, and useful in README files and documentation.

## Later Backends

Later renderer backends may include bitmap export, Win32/GDI+, Direct2D, Skia, Cairo, HTML Canvas, or terminal-oriented experiments. These should be added only after the core scene model and coordinate mapping are stable enough.
