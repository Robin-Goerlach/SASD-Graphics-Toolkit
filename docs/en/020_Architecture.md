# Architecture
Document ID: GFX-DOC-ARCHITECTURE.

## ADR-GFX-001: Two independent language dimensions — accepted
Follow the Math Toolkit convention: `src/<platform>/`, `tests/<platform>/`,
`samples/<platform>/`, `spec/` and `docs/<locale>/`.
Use the existing platform key `dotnet` for C#/.NET and `cpp` for C++.
Do not create combinations such as `src/cpp/de/` or translated source copies.
English is the default documentation language; German is a companion.
Additional implementation platforms and documentation locales are additive.

## ADR-GFX-002: Peer implementations — accepted
C++20/CMake is first. C#/.NET is a planned idiomatic peer implementation,
not an obligatory wrapper around C++. Shared behavior is authoritative;
source sharing and identical API spelling are not required.
A language binding delegates to another implementation and must be identified
as a binding. Optional bindings/native performance providers need a separate
decision covering ownership, error conversion, packaging and deployment.
No C ABI or .NET project is implemented by this structural change.

## Graphics layers
Applications and samples supply domain data. Visualizers build scenes.
Scenes contain layers, shapes and presentation styles.
Coordinate mapping places those objects; a renderer translates them to output.
The first renderer is SVG. Boards/grids and small charts follow.
The core has no dependency on a UI framework, game rules or game AI.

Planned C++ namespaces: `sasd::graphics::{geometry,coordinates,style,scene,boards,charts}`
and `sasd::graphics::rendering::svg`.
The planned .NET namespace root is `Sasd.Graphics`.
These are design directions, not existing public APIs.

## ADR-GFX-003: Math ownership and integration — proposed
Math owns reusable mathematical algorithms and primitives; Graphics owns scenes,
styles, visual coordinate mapping, rendering and visualization.
Do not independently recreate a general vector/matrix/numerics library in Graphics.
The preferred future path is a small Math C++ geometry module for C++ Graphics and
the existing Math .NET tree for .NET Graphics, with explicit adapters as needed.
The concrete package boundary, versions and API are still open.
Graphics currently neither links Math nor embeds a .NET runtime.

Keep the Math core independent of Graphics. Applications/samples may combine both.
See [integration](040_Integration_GameWorks_Numerics.md) before adding a dependency.

## Verification
Shared input/output cases and tolerances live in `spec/`.
Language-specific runners will execute them once implementations exist.
Compare geometry and SVG semantics; do not require byte-identical SVG or
pixel-identical font rendering across backends.
