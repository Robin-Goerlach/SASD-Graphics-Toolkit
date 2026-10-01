# Contributing

Thank you for your interest in **SASD Graphics Toolkit**.

English is the default documentation language. The German companion file is [CONTRIBUTING.de.md](CONTRIBUTING.de.md).

## Current Status

The project is in the repository-baseline and concept phase. Contributions should therefore focus on clarity, structure, small core building blocks, and tests.

## Preferred Contribution Style

- Keep changes small and understandable.
- Update documentation together with code changes.
- Do not add broad abstractions without a concrete demo or test case.
- Keep the core independent of UI frameworks.
- Prefer deterministic tests.

## Scope Rules

Suitable contributions:

- core geometry types,
- coordinate mapping,
- scene model primitives,
- SVG export,
- board/grid helpers,
- simple chart foundations,
- tests and documentation.

Out of scope:

- game rules,
- game AI,
- numerical algorithms,
- large UI frameworks,
- unrelated application logic.

## Build

```bash
cmake -S . -B build
cmake --build build
ctest --test-dir build
```

## Documentation Language

Public default files should be English. German companion files should use the `.de.md` suffix and should stay close to the English version.
