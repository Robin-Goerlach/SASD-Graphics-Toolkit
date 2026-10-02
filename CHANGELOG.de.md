# Changelog
[English](CHANGELOG.md). Noch kein öffentliches Release.

## Unreleased
### Hinzugefügt
- Math-kompatible C++-/.NET-Quell-, Test- und Beispielbäume.
- Vertragsentwürfe, vier affine Referenzvektoren und Plattform-/Sprachstandsregistrierung.
- Englische/deutsche Fachtextordner, stabile Dokument-IDs und geprüfte Quellhashes.
- Leere UTF-8-Textkataloge; Repository-/Link-/Übersetzungs-/Katalogprüfung mit Python und CI.
- Unterstützungsmatrix und ausdrückliche Entscheidungen zu gleichrangigen Implementierungen.

### Geändert
- CMake delegiert an src/cpp, tests/cpp und samples/cpp.
- Deutsche Fachtexte liegen in docs/de statt in flachen .de.md-Dateien.
- Alte nummerierte Dokumentations- und include-Pfade behalten Migrationshinweise.
- Integrationsregeln erlauben eine vorgeschlagene kleine Math-Geometrieabhängigkeit; Math-Core bleibt unabhängig.

### Noch nicht implementiert
Grafikbibliothek/API, Renderer, .NET-Projekt, Pakete, ausführbare Beispiele,
Lokalisierungslaufzeit und Cross-Language-Konformitätsrunner.

## Ursprüngliche Repository-Grundlage
C++20-/CMake-Gerüst, zweisprachige Übersicht/Features/Architektur/Roadmap, MIT-Lizenz,
SVG-Konzeptvorschau und Ubuntu-/Windows-CI.
