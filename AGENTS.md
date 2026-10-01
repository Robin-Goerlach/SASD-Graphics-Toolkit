# AGENTS.md

Arbeitsregeln für Codex/AI-gestützte Entwicklung im Repository **SASD Graphics Toolkit**.

## Projektzweck

Dieses Repository entwickelt einen modernen **C++-2D-Grafik-Unterbau** für SASD-Projekte. Der Fokus liegt auf sauber getrennten Kernmodellen, Geometrie, Koordinaten, Rendering und exportierbaren Visualisierungen.

## Wichtige Abgrenzung

- Keine Spielregeln in dieses Repository aufnehmen.
- Keine numerischen Fachalgorithmen in dieses Repository aufnehmen.
- Keine UI- oder Rendering-Framework-Typen in den Core übernehmen.
- Keine unnötig große Architektur bauen, bevor eine Demo sie benötigt.

## Zielarchitektur

```text
sasd_graphics_core
    keine UI-Abhängigkeit

sasd_graphics_rendering_svg
    erster Renderer und primäres Test-/Dokumentationsziel

sasd_graphics_boards
    Grid-, Board- und Hit-Testing-Hilfen

sasd_graphics_charts
    einfache Visualisierung von Datenserien

sasd_graphics_demo
    spätere interaktive oder dateibasierte Demo
```

## Entwicklungsstil

- Code klar und nachvollziehbar kommentieren.
- Öffentliche Typen und Funktionen dokumentieren.
- Kleine, testbare Klassen und freie Funktionen bevorzugen.
- Keine Magie in Rendering- oder Transformationscode verstecken.
- Beispiele und Tests mitliefern, sobald neue Konzepte eingeführt werden.
- Bestehende Dokumentation aktualisieren, wenn Architekturentscheidungen geändert werden.

## Empfohlene Reihenfolge

1. CMake-Projektstruktur anlegen.
2. `sasd_graphics_core` erstellen.
3. Geometrietypen implementieren.
4. Tests für Geometrietypen ergänzen.
5. Scene Model minimal einführen.
6. SVG Renderer minimal einführen.
7. Go-Moku-Board als erste echte Demo erzeugen.

## Build und Test

Aktuell existiert noch kein produktiver Code. Sobald die CMake-Struktur angelegt ist, sollen diese Befehle funktionieren:

```bash
cmake -S . -B build
cmake --build build
ctest --test-dir build
```

## Commit- und PR-Regeln

- Kleine, nachvollziehbare Änderungen.
- Dokumentation und Tests zusammen mit Fachänderungen pflegen.
- README nur mit tatsächlich erreichten Features aktualisieren oder klar als Roadmap kennzeichnen.
- Keine großen Refactorings ohne sichtbaren Nutzen.

## Namenskonventionen

Vorgeschlagene Namespaces:

```text
sasd::graphics
sasd::graphics::geometry
sasd::graphics::styling
sasd::graphics::scene
sasd::graphics::rendering
sasd::graphics::boards
sasd::graphics::charts
```

Vorgeschlagene Include-Pfade:

```text
#include <sasd/graphics/geometry/point.hpp>
#include <sasd/graphics/scene/scene.hpp>
#include <sasd/graphics/rendering/svg_renderer.hpp>
```

## Qualitätskriterien

Eine Änderung ist erst dann wirklich gut, wenn sie:

- fachlich klar abgegrenzt ist,
- Tests oder nachvollziehbare Demo-Ausgabe besitzt,
- keine unnötigen Abhängigkeiten einführt,
- dokumentiert ist,
- langfristig wiederverwendbar bleibt.
