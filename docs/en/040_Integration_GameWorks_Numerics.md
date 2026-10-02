# Integration with Math, GameWorks and UI
Document ID: GFX-DOC-INTEGRATION.

## Responsibilities
Math owns reusable mathematical algorithms and general geometry/transforms.
Graphics owns scene models, styles, renderers, visual coordinate mapping,
boards and chart presentation. GameWorks owns rules, game state and AI.
UI projects own widgets and interaction.

## Dependency decision
The previous blanket rule forbidding any Graphics-to-Math dependency is superseded
by proposed ADR-GFX-003 in [architecture](020_Architecture.md).
Preferred future direction: Graphics may consume a small Math geometry module.
Math core must not depend on Graphics, UI or a renderer.
A numerical visualization application/sample composes Math and Graphics.
Do not make the entire Math library depend on Graphics for its sample charts.

There is no configured Math package/link/runtime dependency today.
The existing Math implementation is C#/.NET; this repository starts with C++.
Directory symmetry alone does not make .NET types usable by C++.
A compatible Math C++ subset or an explicitly approved interoperability boundary
must exist before claiming direct native integration.
Review actual package/license/API requirements when selecting the dependency.

## Consumers
GameWorks and UI may consume Graphics. Graphics does not consume their cores.
Adapters convert domain data into scenes outside the reusable graphics core.
The first scenario remains a small Go-Moku SVG board with no embedded rules.

## Coordinate boundary
Mathematical vectors/transforms belong in Math; world-to-output conventions,
viewport sizing and visible styles belong in Graphics.
Specify units, axis direction and conversion ownership at the adapter boundary.
Avoid both hidden circular dependencies and duplicate general math implementations.
