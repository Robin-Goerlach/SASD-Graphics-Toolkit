# AGENTS.md

Arbeitsregeln für Codex/AI-gestützte Entwicklung im Repository **SASD Graphics Toolkit**.

## Projektzweck

Dieses Repository entwickelt einen modernen 2D-Grafik-Unterbau für SASD-Projekte. Der Fokus liegt auf sauber getrennten Kernmodellen, Geometrie, Koordinaten, Rendering und exportierbaren Visualisierungen.

## Wichtige Abgrenzung

- Keine Spielregeln in dieses Repository aufnehmen.
- Keine numerischen Fachalgorithmen in dieses Repository aufnehmen.
- Keine UI-Framework-Typen in den Core übernehmen.
- Keine unnötig große Architektur bauen, bevor eine Demo sie benötigt.

## Zielarchitektur

```text
Sasd.Graphics.Core
    keine UI-Abhängigkeit

Sasd.Graphics.Rendering.Svg
    erster Renderer und primäres Test-/Dokumentationsziel

Sasd.Graphics.Boards
    Grid-, Board- und Hit-Testing-Hilfen

Sasd.Graphics.Charts
    einfache Visualisierung von Datenserien

Sasd.Graphics.DemoApp
    spätere interaktive Demo, zunächst nicht zwingend
```

## Entwicklungsstil

- Code klar und nachvollziehbar kommentieren.
- Öffentliche Typen mit XML-Dokumentation versehen.
- Kleine, testbare Klassen bevorzugen.
- Keine Magie in Rendering- oder Transformationscode verstecken.
- Beispiele und Tests mitliefern, sobald neue Konzepte eingeführt werden.
- Bestehende Dokumentation aktualisieren, wenn Architekturentscheidungen geändert werden.

## Empfohlene Reihenfolge

1. Solution und Projektstruktur anlegen.
2. `Sasd.Graphics.Core` erstellen.
3. Geometrietypen implementieren.
4. Tests für Geometrietypen ergänzen.
5. Scene Model minimal einführen.
6. SVG Renderer minimal einführen.
7. Go-Moku-Board als erste echte Demo erzeugen.

## Build und Test

Aktuell existiert noch kein produktiver Code. Sobald die Solution angelegt ist, soll diese Sektion konkretisiert werden.

Geplante Befehle:

```bash
dotnet restore
dotnet build
dotnet test
```

## Commit- und PR-Regeln

- Kleine, nachvollziehbare Änderungen.
- Dokumentation und Tests zusammen mit Fachänderungen pflegen.
- README nur mit tatsächlich erreichten Features aktualisieren oder klar als Roadmap kennzeichnen.
- Keine großen Refactorings ohne sichtbaren Nutzen.

## Namenskonventionen

Vorgeschlagene Namespaces:

```text
Sasd.Graphics.Core
Sasd.Graphics.Core.Geometry
Sasd.Graphics.Core.Styling
Sasd.Graphics.Core.SceneGraph
Sasd.Graphics.Rendering.Svg
Sasd.Graphics.Boards
Sasd.Graphics.Charts
```

## Qualitätskriterien

Eine Änderung ist erst dann wirklich gut, wenn sie:

- fachlich klar abgegrenzt ist,
- Tests oder nachvollziehbare Demo-Ausgabe besitzt,
- keine unnötigen Abhängigkeiten einführt,
- dokumentiert ist,
- langfristig wiederverwendbar bleibt.
