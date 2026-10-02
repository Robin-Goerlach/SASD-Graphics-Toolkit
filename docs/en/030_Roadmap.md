# Roadmap
Document ID: GFX-DOC-ROADMAP.

## M0: Multi-language repository foundation — complete
Math-compatible platform trees; English/German documentation; development rules;
draft contracts and affine reference vectors; support matrix; CMake delegation;
repository/link/translation/resource validation in CI.
No graphics algorithm, library target or cross-language runner is implemented.

## M1: Small mathematical/geometry boundary — planned
Resolve ADR-GFX-003 with Math Toolkit. Identify only the 2D types and operations
needed by the first demo. Specify finite inputs, ownership, units and tolerances.
Acceptance: documented dependency/API choice and meaningful unit tests for the
first actual C++ types. A complete Math C++ port is not a prerequisite.

## M2: Coordinates — planned
Viewport, world/output mapping, scale, translation, y-axis convention and bounds.
Run the affine reference vectors through actual C++ operations, including inverse
round trips and invalid-input cases.

## M3: Scene and styles — planned
Layers, basic shapes, stroke/fill/text, stable IDs and z-order.

## M4: SVG — planned
Lines, rectangles, circles, polylines/text, viewBox, XML escaping, Unicode and
locale-independent number serialization. Test structure and coordinates.

## M5: Boards — planned
Generic grid, Go-Moku demo, chess baseline, markers and hit testing.
Keep all game rules outside the toolkit.

## M6: Charts — planned
Axes, line/scatter series, legends and sample integration with Math.
Separate localized visible labels from technical SVG number serialization.

## M7: Second implementation — planned, consumer-driven
Select a useful C#/.NET slice rather than promising an immediate complete port.
Build/test/pack it independently; use shared reference vectors in both runners.
Document supported capabilities and normal language-specific error/API conventions.
Additional platforms are considered only when a concrete consumer needs them.

## M8: Pre-release — planned
API review, real build/test/package gates and small runnable examples.
Update support status only with executable evidence.
