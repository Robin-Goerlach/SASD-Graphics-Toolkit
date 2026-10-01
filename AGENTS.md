# AGENTS.md

Development rules for Codex/AI-assisted work in the **SASD Graphics Toolkit** repository.

English is the default documentation language. The German companion file is [AGENTS.de.md](AGENTS.de.md).

## Project Purpose

This repository develops a modern C++20 2D graphics foundation for SASD projects. The focus is on cleanly separated geometry, coordinates, styling, scene modeling, rendering, and exportable visualizations.

## Boundaries

Do not add the following to this repository:

- game rules,
- chess or Go-Moku AI,
- numerical algorithms,
- UI-framework core logic,
- unnecessary large abstractions before a demo needs them.

## Target Architecture

```text
sasd::graphics::geometry
sasd::graphics::coordinates
sasd::graphics::style
sasd::graphics::scene
sasd::graphics::rendering::svg
sasd::graphics::boards
sasd::graphics::charts
```

## Coding Rules

- Use C++20.
- Keep public API names clear and conservative.
- Prefer small types with tests over large untested frameworks.
- Keep core code independent of Win32, Qt, GTK, Skia, Cairo, and other concrete rendering frameworks.
- Add comments where they explain intent, invariants, or non-obvious decisions.

## Documentation Rules

- Public default documentation is English.
- German companion documents use `.de.md`.
- Do not claim planned features are already implemented.
- Keep README, docs, and roadmap aligned with the actual state of the repository.

## Testing Rules

- Test geometry and coordinate mapping without UI dependencies.
- Prefer deterministic tests.
- SVG tests should validate structure and coordinates rather than relying only on pixel comparisons.

## First Implementation Priority

1. Core geometry.
2. Coordinate mapping.
3. Scene and style model.
4. SVG renderer.
5. Go-Moku board demo.
