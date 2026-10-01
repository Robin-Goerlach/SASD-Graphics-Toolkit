# AGENTS.de.md

Arbeitsregeln für Codex-/KI-gestützte Entwicklung im Repository **SASD Graphics Toolkit**.

Englisch ist die Standardsprache der Dokumentation. Die englische Standarddatei ist [AGENTS.md](AGENTS.md).

## Projektzweck

Dieses Repository entwickelt einen modernen C++20-2D-Grafik-Unterbau für SASD-Projekte. Der Fokus liegt auf sauber getrennter Geometrie, Koordinatenlogik, Styling, Szenenmodellierung, Rendering und exportierbaren Visualisierungen.

## Abgrenzung

Folgendes gehört nicht in dieses Repository:

- Spielregeln,
- Schach- oder Go-Moku-KI,
- numerische Algorithmen,
- UI-Framework-Core-Logik,
- unnötig große Abstraktionen, bevor eine Demo sie benötigt.

## Zielarchitektur

```text
sasd::graphics::geometry
sasd::graphics::coordinates
sasd::graphics::style
sasd::graphics::scene
sasd::graphics::rendering::svg
sasd::graphics::boards
sasd::graphics::charts
```

## Coding-Regeln

- C++20 verwenden.
- Öffentliche API-Namen klar und konservativ halten.
- Kleine Typen mit Tests sind besser als große ungetestete Frameworks.
- Der Core bleibt unabhängig von Win32, Qt, GTK, Skia, Cairo und anderen konkreten Rendering-Frameworks.
- Kommentare sollen Absicht, Invarianten oder nicht offensichtliche Entscheidungen erklären.

## Dokumentationsregeln

- Öffentliche Standarddokumentation ist Englisch.
- Deutsche Begleitdokumente verwenden `.de.md`.
- Geplante Funktionen dürfen nicht als bereits implementiert beschrieben werden.
- README, Docs und Roadmap müssen zum tatsächlichen Repository-Stand passen.

## Testregeln

- Geometrie und Koordinaten-Mapping ohne UI-Abhängigkeiten testen.
- Deterministische Tests bevorzugen.
- SVG-Tests sollen Struktur und Koordinaten prüfen, nicht nur Pixel vergleichen.

## Erste Implementierungspriorität

1. Core Geometry.
2. Coordinate Mapping.
3. Scene und Style Model.
4. SVG Renderer.
5. Go-Moku-Board-Demo.
