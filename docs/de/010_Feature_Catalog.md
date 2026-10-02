# Feature-Katalog

Dieses Dokument sammelt die geplanten Funktionsbereiche des **SASD Graphics Toolkit**. Die Liste ist nach Abhängigkeiten und praktischer Umsetzungspriorität geordnet.

## P0 – Repository- und Dokumentationsbasis

- Englisches README als Standard-Einstieg.
- Deutsches Begleit-README.
- Dokumentationsverzeichnis.
- Architekturüberblick.
- Roadmap.
- AGENTS.md für KI-gestützte Entwicklung.
- MIT-Lizenzinformation.

## P1 – Core Geometry

Grundlage für alle späteren Module:

- `point2d`
- `size2d`
- `vector2d`
- `rect2d`
- `line_segment2d`
- `circle2d`
- `polygon2d`
- `bounds2d`

Basisoperationen:

- Distanzberechnung,
- Bounds-Berechnung,
- einfache Schnitt- und Enthält-Prüfungen,
- Normalisierung von Rechtecken,
- Mapping zwischen Welt- und Ausgabe-Koordinaten.

## P2 – Styling

Styles beschreiben Darstellung, nicht Fachlogik:

- Farben,
- Linienbreite,
- Linienart,
- Füllstil,
- Textstil,
- Symbolstil,
- Themes.

Der Core sollte ein eigenes einfaches Stilmodell verwenden und keine Win32-, Qt-, GTK-, Skia- oder Cairo-Typen direkt nach außen tragen.

## P3 – Scene Model

Das Scene Model beschreibt, was gezeichnet werden soll:

- Linie,
- Rechteck,
- Kreis/Ellipse,
- Polygon,
- Pfad,
- Text,
- Layer,
- Gruppe,
- Z-Order,
- optionale IDs für Hit-Testing und Debugging.

## P4 – SVG Renderer

SVG ist das empfohlene erste Ausgabeformat, weil es textbasiert, gut testbar, Markdown-tauglich und unabhängig von nativen UI-Frameworks ist.

Mindestumfang:

- Linien,
- Rechtecke,
- Kreise,
- einfache Pfade,
- Text,
- Styles,
- ViewBox,
- Export nach `.svg`.

## P5 – Boards und Grids

Geplante Brett-/Rasterfunktionen:

- Go-Moku-Brett, 19 × 19,
- Schachbrett, 8 × 8,
- generisches Zellraster,
- Karten-Layoutbereiche für spätere Bridge-/Kartendemos,
- Zellbeschriftungen,
- Hervorhebung ausgewählter Felder oder letzter Züge,
- Mapping von Ausgabeposition auf Brettkoordinate,
- Mapping von Brettkoordinate auf Mittelpunkt.

## P6 – Charts

Diagramme sollen klein anfangen:

- Funktionsplot,
- Polyline-Plot,
- Scatterplot,
- Balkendiagramm,
- einfache Achsen,
- einfache Legende.

Spätere Kandidaten:

- Histogramm,
- Boxplot,
- Heatmap,
- Suchbaumvisualisierung,
- Bewertungsverlauf für Game-AI.

## P7 – Renderer-Backends

Mögliche spätere Backends:

| Backend | Zweck |
|---|---|
| Bitmap | Bildexport für Dokumentation und Tests |
| Win32/GDI+ | einfaches Windows-Demo-Backend |
| Direct2D | späteres performanteres Windows-Backend |
| Skia | plattformübergreifendes 2D-Rendering |
| Cairo | plattformübergreifendes 2D-Rendering, besonders Linux-nah |
| Terminal/Sixel | experimentelle terminalnahe Visualisierung |
| HTML Canvas | späterer Web-/Dokumentations-Export |

## P8 – Demos

Demos sollen klein bleiben und jeweils ein Konzept erklären:

- `demo_gomoku_board`
- `demo_function_plot`
- `demo_transforms`
- `demo_chess_board`
- `demo_svg_export`

## P9 – Tests

Testbereiche:

- Geometrie,
- Koordinatentransformationen,
- Bounds,
- Board-Mapping,
- SVG-Ausgabe,
- Chart-Skalierung.

Viele Tests sollten modell- oder textbasiert sein, zum Beispiel durch Prüfung von SVG-Elementen, Koordinaten und Bounds statt ausschließlich durch Pixelvergleiche.

## Mehrsprachige Grundlage

Dokument-ID: GFX-DOC-FEATURES. C++20 ist die erste Implementierung; C#/.NET ist als gleichrangige Variante geplant. Noch ist keine Grafikbibliothek implementiert. Gemeinsames Verhalten gehört in `spec/`; sprachspezifischer Code, Tests und Beispiele verwenden `src/<plattform>/`, `tests/<plattform>/` und `samples/<plattform>/`. Für mathematische Grundtypen und Algorithmen muss vor der Implementierung die Zuständigkeit mit dem Math Toolkit geklärt werden.

Siehe [Architektur](020_Architecture.md), [Verträge](060_Contracts.md) und [Unterstützungsstand](070_Language_Support.md).
