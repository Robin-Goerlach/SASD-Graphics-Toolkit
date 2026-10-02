# Shared graphics contracts — draft
Document ID: GFX-DOC-CONTRACTS.

These contracts guide implementation; no graphics API currently executes them.
[spec/contracts.json](../../spec/contracts.json) contains stable IDs and requirements.
[Affine reference vectors](../../spec/test-vectors/affine2d.json) are input/output
data, not an implemented cross-language test suite.

## GFX-COORD-001: Affine mapping
For matrix coefficients `[a,b,c,d,tx,ty]` and point `[x,y]`:
`x' = a*x + c*y + tx`; `y' = b*x + d*y + ty`.
This formula fixes the serialization convention, not a language's matrix memory layout.
Finite inputs and finite expected outputs are required for these reference cases.
Compare each component using
`abs(actual-expected) <= max(absTol, relTol*abs(expected))`.
Reference cases use absolute and relative tolerance 1e-12.
These are case-specific tolerances, not a universal geometry precision guarantee.
Units, coordinate-axis choices, inverse handling, singular matrices and invalid
inputs must be specified before exposing the corresponding public APIs.

## GFX-SVG-001: Technical numbers
SVG attributes use locale-independent decimal points and finite numeric values.
A German visible axis label can show `1,5` while the SVG coordinate remains `1.5`.
Rounding/precision rules and boundary tests are required before implementation.

## GFX-TEXT-001: Text
Preserve Unicode user text and XML-escape it correctly in SVG text/attribute context.
Preserving text does not promise a particular backend's fonts or glyph shaping.

## GFX-DEP-001: Dependencies
The core is independent from UI frameworks, game rules and game AI.
Math-core dependency direction is specified in ADR-GFX-003; exact integration is open.

## Glossary
| Stable term | German explanation |
|---|---|
| scene | Szene: description of drawing objects / Beschreibung der Zeichenobjekte |
| viewport | Viewport: output region / Ausgabebereich |
| bounds | Begrenzung: spatial extent / räumliche Ausdehnung |
| stroke | Kontur: line appearance / Liniengestaltung |
| fill | Füllung: interior appearance / Flächengestaltung |
| conformance | Konformität: satisfying shared behavior / gemeinsames Verhalten erfüllen |

Future contracts cover bounds edges, normalization, clipping, z-order, error semantics
and SVG comparisons. Add contracts when the first API needs them.
