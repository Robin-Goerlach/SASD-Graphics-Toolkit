# Language support
Document ID: GFX-DOC-SUPPORT.

## Implementation platforms
| Platform | Kind | Current evidence | Graphics capabilities |
|---|---|---|---|
| cpp | peer implementation, first | C++20/CMake scaffold, repository CTest check | none implemented |
| dotnet | planned peer implementation | reserved source/test/sample paths | none implemented |

No library target, .NET project, package, renderer, executable sample or
cross-language conformance runner exists yet.
The CMake/CTest gate validates repository consistency only.
Support metadata is recorded in [project.json](../../spec/project.json).

## Human languages
| Locale | Documentation | Message catalogs | Runtime |
|---|---|---|---|
| en | default, available | empty UTF-8 JSON scaffold | not implemented |
| de | companion, available | empty UTF-8 JSON scaffold | not implemented |

## Adding support
Create platform paths only with an explicit scope. Add actual build, tests,
samples and shared-vector runners before marking capabilities implemented.
For another documentation locale, register translations and reviewed source hashes.
Catalog key parity does not imply correct translations or font/shaping support.
