# Roadmap

Diese Roadmap beschreibt eine sinnvolle Entwicklungsreihenfolge für das **SASD Graphics Toolkit**. Sie ist bewusst so aufgebaut, dass früh sichtbare Ergebnisse entstehen, ohne die Architektur zu früh zu überfrachten.

## M0 – Repository Baseline

Ziel: Das öffentliche Repository verständlich machen und für Entwicklung vorbereiten.

Ergebnis:

- englisches README als Standard,
- deutsche Begleitdokumentation,
- SVG-Vorschau,
- Dokumentationsverzeichnis,
- Architekturüberblick,
- Feature-Katalog,
- AGENTS.md,
- CMake-Basis,
- MIT-Lizenz bestätigt.

## M1 – Core Geometry

Ziel: Fundament für alle späteren Grafikfunktionen schaffen.

Umfang:

- `point2d`
- `size2d`
- `vector2d`
- `rect2d`
- `line_segment2d`
- `bounds2d`

Akzeptanzkriterien:

- Unit-Tests für alle öffentlichen Typen.
- Keine Abhängigkeit auf UI-Frameworks.
- Öffentliche Typen haben klare Kommentare und Beispiele.

## M2 – Coordinate Mapping

Ziel: Umrechnung zwischen Modell-, Welt- und Ausgabe-Koordinaten.

Umfang:

- Viewport,
- World-to-device Mapping,
- Skalierung,
- Translation,
- optionale Y-Achsen-Invertierung,
- einfaches Bounds-Clipping.

## M3 – Scene Model und Styles

Ziel: Zeichnungen als testbare Modelle beschreiben.

Umfang:

- Scene,
- Layer,
- Shape-Primitive,
- Stroke/Fill/Text Styles,
- einfache Z-Order.

## M4 – SVG Renderer

Ziel: sichtbare Ausgabe aus dem Scene Model erzeugen.

Umfang:

- Linien,
- Rechtecke,
- Kreise,
- Text,
- einfache Pfade/Polylines,
- ViewBox-Unterstützung.

## M5 – Board Renderer

Ziel: Visualisierung für GameWorks Lab vorbereiten.

Umfang:

- generisches Raster,
- Go-Moku-Brett,
- Schachbrett-Basis,
- Koordinatenbeschriftungen,
- Marker/Steine/Platzhalter,
- Hit-Testing.

## M6 – Chart Basics

Ziel: erste nützliche Visualisierung für Numerics/Math Toolkit bereitstellen.

Umfang:

- Achsen,
- Skalierung,
- Polyline-Serien,
- Scatter-Serien,
- einfache Legende,
- Funktionsplot-Demo.

## M7 – Demo-Anwendung

Ziel: praktisches visuelles Testbett schaffen.

Umfang:

- kleine Demo-App oder Kommandozeilen-Demogenerator,
- Board-Vorschau,
- Chart-Vorschau,
- SVG-Export,
- Koordinaten-/Hit-Test-Diagnose.

## M8 – Stabilisierung und erstes Pre-Release

Ziel: erste nutzbare Vorschauversion vorbereiten.

Umfang:

- API-Review,
- Dokumentation aufräumen,
- Beispiele aufräumen,
- CI prüfen,
- Release Notes.

## Prioritätsregel

Im Zweifel ist eine kleine funktionierende Demo mit Tests besser als ein großes abstraktes Framework.
