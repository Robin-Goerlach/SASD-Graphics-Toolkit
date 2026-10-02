# Additional Project Context from the GameWorks Discussion

> **Document type:** non-normative project context
>
> **Default language:** English. German companion: [090_Conversation_Context.md](../de/090_Conversation_Context.md)
>
> This document preserves decisions, ideas, boundaries, reference products, and visual direction for **SASD Graphics Toolkit** that emerged in a broader discussion originally centered on **SASD GameWorks Lab**. It exists because several of those points are important for the Graphics Toolkit itself but only indirectly relevant to GameWorks.
>
> The normative project direction remains the dedicated project overview, architecture, feature catalog, roadmap, and future ADRs. When this context document conflicts with a newer dedicated document or implemented code, the newer dedicated source wins.

## Current policy after repository restructuring

Document ID: GFX-DOC-CONTEXT. The following sections preserve the historical discussion.
The current [architecture](020_Architecture.md) supersedes older C++-only language,
flat-documentation and geometry-ownership statements: C++ is first, C#/.NET is a planned
peer, locale folders are canonical, and the small Math boundary is proposed ADR-GFX-003.
The [language support matrix](070_Language_Support.md) records actual implementation status.

## 1. Why the Graphics Toolkit emerged

The broader GameWorks discussion started from a modern reinterpretation of Borland's historical Turbo GameWorks concept. GameWorks needs visual building blocks for board games, analysis, diagrams, and teaching examples. At the same time, other SASD projects need many of the same low-level capabilities.

This led to a key decision: shared graphics functionality should not be copied into each application. Instead, **SASD Graphics Toolkit should be an independent reusable library** that can serve GameWorks and other SASD projects.

The same reasoning applies to numerical functionality: GameWorks may consume both a graphics toolkit and a numerics/math toolkit, but it should not own either one.

## 2. Core architectural decision

The preferred long-term structure is conceptually:

```text
SASD GameWorks Lab
    |
    +--> SASD Graphics Toolkit
    |
    +--> SASD Numerics / Math Toolkit

Other SASD applications
    |
    +--> SASD Graphics Toolkit
    +--> SASD Numerics / Math Toolkit
```

The libraries remain independently useful. GameWorks is an important requirements driver, not the owner of the abstractions.

A practical rule discussed in the conversation was:

> Extract a reusable abstraction when it is clearly generic or when the same capability would otherwise be implemented more than once.

This deliberately avoids two extremes:

- duplicating geometry, plotting, board rendering, and export logic in every application;
- building a huge abstract graphics framework before a real application needs it.

The implementation should therefore be **use-case driven but architecturally independent**.

## 3. Current technology direction

An early conceptual stage briefly discussed C#-oriented graphics modules with WinForms/WPF adapters because the first GameWorks application idea was framed as a .NET desktop application. That was exploratory and is superseded for this repository.

The dedicated repository direction established later in the discussion is:

- **C++20** as the implementation language;
- **CMake** as the build system;
- a framework-neutral graphics core;
- renderer backends added behind clear boundaries;
- English documentation as the default, with German companion documents.

WinForms/WPF can still be consumers through adapters or bindings in the wider SASD ecosystem, but they must not define the Graphics Toolkit core model.

## 4. Separation of responsibilities

A central design principle discussed repeatedly is the separation of four concerns:

```text
Graphics model      -> what should be drawn?
Layout/coordinates  -> where and at which scale?
Renderer backend    -> how is it emitted or displayed?
Application logic   -> why is it drawn?
```

This gives the following project boundaries:

### SASD Graphics Toolkit owns

- 2D geometry and bounds;
- coordinate mapping and viewports;
- graphical scene descriptions;
- styles and themes at an abstract level;
- reusable board/grid visual primitives;
- chart and plotting primitives;
- rendering adapters/exporters;
- hit-testing and coordinate conversion where they are graphical concerns;
- examples and visualization-focused tests.

### SASD GameWorks Lab owns

- game rules;
- legal move generation;
- game states;
- game AI and search policy;
- chess, Go-Moku, Bridge, or other domain logic;
- interpretation of game analysis.

### SASD Numerics / Math Toolkit owns

- mathematical and numerical algorithms;
- statistics and numerical procedures;
- numerical optimization;
- mathematical data preparation;
- domain-level computation behind plots.

### SASD UI Toolkit / UI Platform owns

- interaction widgets and application UI concepts;
- controls, menus, focus, command handling, and higher-level UI behavior;
- native UI integration beyond the rendering responsibilities of Graphics Toolkit.

The intention is to avoid circular ownership and hidden coupling between the projects.

## 5. Feature areas identified in the conversation

The discussion produced the following feature groups for the Graphics Toolkit.

### 5.1 Core geometry

Initial reusable types include:

- `point2d`
- `size2d`
- `vector2d`
- `rect2d`
- `bounds2d`
- `line_segment2d`
- `circle2d`
- `polygon2d`

Relevant operations include distance, containment, bounds calculation, simple intersections, rectangle normalization, and mapping between coordinate systems.

### 5.2 Coordinate systems and transformations

The toolkit should support a clean distinction between model/world coordinates and output/device coordinates.

Topics discussed include:

- viewport definition;
- translation;
- scaling;
- rotation where appropriate;
- optional Y-axis inversion;
- world-to-device and device-to-world mapping;
- simple clipping and bounds handling;
- board-coordinate to device-coordinate mapping;
- device-position to board-cell/intersection hit-testing.

### 5.3 Scene model

A scene should describe a drawing without knowing the final rendering technology.

Potential concepts include:

- scene;
- layer;
- group;
- z-order;
- shape primitives;
- stable IDs for hit-testing/debugging;
- line, rectangle, circle/ellipse, polygon, path, text;
- image references later.

### 5.4 Styling

Styling should be renderer-neutral rather than based on Win32, Qt, Skia, Cairo, WPF, or another framework's concrete types.

Discussed style concepts include:

- colors;
- strokes;
- fill styles;
- line width and line type;
- text styles;
- symbol styles;
- themes.

### 5.5 Rendering and export

The preferred first renderer is **SVG** because it is:

- text based;
- easy to inspect and test;
- well suited to Markdown and repository documentation;
- independent from native UI frameworks;
- useful for deterministic demo output.

Possible later outputs/backends discussed include:

- bitmap export (PNG/BMP/JPEG depending on backend);
- Win32/GDI+;
- Direct2D;
- Skia;
- Cairo;
- HTML Canvas;
- experimental terminal/Sixel or text-oriented output.

No commitment was made that all of these must be implemented. They are extension candidates behind the renderer boundary.

### 5.6 Boards and grids

GameWorks provides a useful concrete driver for generic board visualization.

Discussed examples include:

- Go-Moku board, especially 19 × 19;
- chess board, 8 × 8;
- generic rectangular cell grid;
- card layout areas for later Bridge or card-game demonstrations;
- coordinate labels;
- markers and pieces;
- selection/highlight state;
- last-move indication;
- hit-testing.

Board rendering should remain graphical; the toolkit should not know whether a move is legal or strategically good.

### 5.7 Charts and mathematical visualization

Graphics Toolkit is also intended to support Numerics/Math projects.

The initial chart direction discussed includes:

- function plots;
- polyline plots;
- scatter plots;
- bar charts;
- axes;
- grid lines;
- labels;
- simple legends.

Possible later visualizations include:

- histograms;
- box plots;
- heat maps;
- search-tree/graph views;
- game-AI evaluation timelines;
- data visualizations and parametric visualizations.

The Graphics Toolkit visualizes data; it should not own statistical or numerical calculation logic.

## 6. Development strategy

A strong theme of the discussion was to avoid building three huge products before obtaining a visible result.

The chosen strategy is:

1. keep Graphics and Numerics as independent projects;
2. let concrete consumers such as GameWorks drive initial requirements;
3. only generalize functions that have clear reusable value;
4. keep the core framework-neutral;
5. get visible output early, with SVG as the first practical target;
6. add backends and advanced abstractions only when justified by real examples.

This can be summarized as:

> Build the applications and extract clean reusable SASD components along the way, rather than designing a perfect universal library in isolation.

## 7. Preferred early demonstrations

Several concrete demonstrations were discussed as useful architecture drivers.

### Go-Moku board

This remains the strongest first demo:

- 19 × 19 board/grid;
- stones rendered as simple circles;
- coordinate labels A–S and 1–19;
- highlighted last move;
- board/device coordinate conversion;
- hit-testing;
- SVG export.

It is small enough to implement quickly but exercises geometry, grids, styles, text, layers, hit-testing, and export.

### Function plot

A function-plot demo can validate:

- world coordinates;
- axes and grids;
- scaling;
- line series;
- clipping;
- labels and annotations.

### Vector-graphics preview

A compact vector demo can validate:

- circles and polygons;
- coordinate transforms;
- shape selection/IDs;
- bounds;
- guides;
- simple geometric annotations.

Together these three demos provide a balanced early test bed for game boards, mathematical plots, and general-purpose 2D graphics.

## 8. Visual application concept discussed in this chat

The original repository preview image created during repository setup was later judged visually weaker than screenshots used for other SASD repositories. A replacement concept was generated in this chat as a **photorealistic desktop application screenshot**.

The preferred visual direction is a polished professional graphics-workbench application rather than a schematic architectural illustration.

The generated concept includes:

- a dark professional desktop application shell;
- project/assets/demos navigation on the left;
- document tabs;
- a **Go-Moku Board** working area;
- a **Function Plot** working area;
- a **Vector Graphics Preview**;
- properties/layers/history panels;
- coordinate-mapping controls;
- SVG-export controls;
- a visual gallery of board, plot, vector, surface, data-visualization, and parametric examples;
- status information such as cursor coordinates, selected geometry, backend, zoom, and export readiness.

This screenshot is an **aspirational product visualization**, not evidence that those features already exist.

The user explicitly preferred this photorealistic application-style screenshot over the current schematic SVG preview and asked for it to become the repository screenshot. The replacement itself should therefore be tracked as a repository presentation task if it has not yet been committed.

## 9. Reference products and projects mentioned

The broader conversation reviewed a range of products. Not all are direct Graphics Toolkit references, but they provide useful context.

### Direct or strong graphics references

**Skia / SkiaSharp**

Relevant as a mature 2D rendering reference for paths, shapes, text, images, filters, and cross-platform rendering. The Graphics Toolkit should not attempt to duplicate all of Skia; Skia is better viewed as a potential backend/reference implementation.

**MonoGame**

Useful as a reference for clear rendering loops, content handling, and approachable C# game/graphics architecture. It is not the architectural target for the toolkit core.

**raylib**

Useful because it deliberately favors a small, understandable API and teaching-friendly examples. This matches the desire for compact demos and low conceptual overhead.

### Adjacent game/AI references

**OpenSpiel** and **Ludii** were discussed primarily for GameWorks architecture and game modeling. Their relevance to Graphics Toolkit is indirect: they reinforce the value of separating game state and game algorithms from visualization.

**Stockfish**, **Leela Chess Zero**, **DDS**, **WBridge5**, and **Bridge Base Online** are domain references for GameWorks rather than direct Graphics Toolkit targets.

### Adjacent numerical references

**Math.NET Numerics**, **ALGLIB**, **NAG**, **IMSL**, and **GSL** were discussed as references for the numerical side of the SASD ecosystem. Their relevance here is the integration boundary: Graphics Toolkit should display numerical results without absorbing those numerical algorithms into the rendering library.

## 10. Repository baseline established in the discussion

During this chat, the repository was expanded from a minimal baseline into a structured project foundation. The following project-level decisions were established:

- public repository: `Robin-Goerlach/SASD-Graphics-Toolkit`;
- C++20/CMake baseline;
- `include/`, `src/`, `tests/`, `docs/`, and `assets/` structure;
- GitHub Actions CMake workflow for Windows and Linux baseline builds;
- project README with screenshot/preview and project boundaries;
- architecture, feature catalog, roadmap, and integration documentation;
- `AGENTS.md` for AI-assisted development;
- contribution and changelog documents;
- **MIT License** retained and explicitly documented.

The repository's existing MIT license was verified in the conversation after an earlier mistaken assumption that the license was still undecided.

## 11. Documentation and language policy

A later explicit user decision established multilingual documentation:

- **English is the default language**.
- German documents are companion versions.
- German companion files use the `.de.md` suffix where practical.
- Public-facing default links should point to English first.
- The English `LICENSE` is legally authoritative.
- `LICENSE.de.md` is only a non-authoritative German reading aid.

The intent is to make additional languages possible later without restructuring the project again.

## 12. Licensing decision

The repository uses the **MIT License**.

This is no longer an open design question for the current repository baseline. Documentation should not describe the license as undecided unless a future deliberate licensing decision supersedes it.

## 13. Product philosophy captured in the discussion

The Graphics Toolkit should be:

- small before it becomes broad;
- understandable and well documented;
- reusable outside GameWorks;
- testable without a GUI;
- backend-independent at its core;
- driven by useful examples;
- suitable for teaching and research as well as application development;
- explicit about the distinction between implemented features and roadmap concepts.

A phrase used to summarize the direction is:

> Do not just draw pixels. Draw models that can be understood, tested, and reused.

## 14. Items that should remain non-normative until separately decided

The conversation also contained ideas that should not silently become commitments:

- exact renderer-backend order after SVG;
- whether all bitmap formats should be supported;
- terminal/Sixel output;
- HTML Canvas export;
- 3D surface rendering;
- advanced parametric visualization;
- exact integration mechanism with SASD UI Toolkit / UI Platform;
- language bindings for C# or other languages;
- packaging and package-manager strategy;
- final public API naming conventions beyond the current C++ direction.

These are useful design candidates, but they require separate decisions, implementation work, or ADRs.

## 15. Practical takeaway

The strongest distilled direction from this chat is:

> **SASD Graphics Toolkit should be a standalone, modern C++20 graphics and visualization foundation, initially driven by real needs from GameWorks and Numerics, but deliberately independent of their domain logic. Start with geometry, coordinate mapping, a scene/style model, SVG, and concrete demos. Expand only when real consumers justify the next abstraction or backend.**
