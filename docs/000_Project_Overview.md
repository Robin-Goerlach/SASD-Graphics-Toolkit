# SASD Graphics Toolkit – Project Overview

## Short Description

**SASD Graphics Toolkit** is planned as a modern 2D graphics foundation for SASD projects. The focus is not an end-user application, but reusable models, drawing operations, coordinate systems, and renderers.

The toolkit is intended to support projects such as **SASD GameWorks Lab**, **SASD Numerics / Math Toolkit**, **SASD UI Toolkit**, and future learning or research tools.

## Why This Project Exists

Several SASD projects need similar visualization features:

- grids and boards for classical games,
- function plots and diagrams for numerics and statistics,
- compact 2D drawings for documentation and analysis,
- exportable visualizations, especially SVG,
- a clean separation between domain model and rendering.

A shared graphics toolkit helps avoid duplicating these concepts across repositories.

## Target Users

- Developers who need testable graphics models without depending on a specific UI framework.
- Readers and learners who want understandable examples for geometry, mapping, and rendering.
- SASD projects that need boards, charts, diagrams, or visual debugging output.

## In Scope

- 2D geometry primitives.
- Coordinate mapping and transformations.
- Scene and layer models.
- SVG as the first renderer/export target.
- Boards, grids, and simple charts.
- Small demos and tests.

## Out of Scope

- A full game engine.
- A complete GUI framework.
- Game rules or AI algorithms.
- Numerical algorithms that belong into SASD Numerics.
- A replacement for Qt, GTK, wxWidgets, Skia, or Cairo.

## Guiding Decisions

1. Keep the core free from UI-framework dependencies.
2. Use SVG early because it is text-based, testable, and useful in documentation.
3. Let real demos drive abstractions.
4. Keep geometry and mapping logic testable without a display.
5. Keep documentation close to implementation decisions.

## First Expected Result

The first useful milestone should provide a small C++20/CMake baseline with core geometry, a simple SVG export path, unit tests, and a small visual demo.
