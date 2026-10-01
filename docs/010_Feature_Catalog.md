# Feature Catalog

Dieses Dokument sammelt die geplanten Funktionsbereiche des **SASD Graphics Toolkit**. Die Liste ist bewusst nach Priorität und Abhängigkeiten geordnet.

## P0 – Repository- und Dokumentationsbasis

Diese Funktionen sind Voraussetzung für strukturierte Entwicklung.

- README mit Zielbild und Screenshot.
- Dokumentationsverzeichnis.
- Roadmap.
- Architekturüberblick.
- AGENTS.md für KI-gestützte Entwicklung.
- klare Entscheidung, dass Core und Renderer getrennt werden.

## P1 – Core Geometry

Grundlage für alle weiteren Module.

### Typen

- `point2d`
- `size2d`
- `vector2d`
- `rect2d`
- `line_segment2d`
- `circle2d`
- `polygon2d`
- `bounds2d`

### Operationen

- Distanzberechnung.
- Bounds-Berechnung.
- Schnitt- und Enthält-Prüfungen, zunächst nur einfache Fälle.
- Normalisierung von Rechtecken.
- Mapping von Weltkoordinaten auf Ausgabe-Koordinaten.

## P2 – Styling

Stile beschreiben die Darstellung, nicht die Fachlogik.

- Farben.
- Linienbreite.
- Linienart.
- Füllung.
- Textstil.
- Symbolstil.
- Themes.

Wichtig: Der Core sollte eigene einfache Stilmodelle besitzen und nicht direkt Win32-, Qt-, GTK-, Skia- oder Cairo-Typen verwenden.

## P3 – Scene Model

Das Scene Model beschreibt, was gezeichnet werden soll.

### Primitive

- Linie.
- Rechteck.
- Kreis/Ellipse.
- Polygon.
- Pfad.
- Text.
- Bildreferenz, später.

### Struktur

- Layer.
- Gruppen.
- Z-Order.
- optionale IDs für Hit-Testing und Debugging.

## P4 – SVG Renderer

SVG ist das erste empfohlene Ausgabeformat.

### Gründe

- textbasiert.
- gut testbar.
- gut in Markdown/README nutzbar.
- kein UI-Framework nötig.
- ideal für Dokumentation und Demos.

### Mindestumfang

- Linien.
- Rechtecke.
- Kreise.
- einfache Pfade.
- Text.
- Styles.
- ViewBox.
- Export als `.svg`.

## P5 – Boards & Grids

Für GameWorks Lab und Lernbeispiele sind Brett- und Rasterdarstellungen besonders wichtig.

### Geplante Boards

- Go-Moku-Board 19 × 19.
- Schachbrett 8 × 8.
- generisches Zellraster.
- Karten-Layoutbereiche für spätere Bridge-/Kartenspiel-Demos.

### Funktionen

- Raster zeichnen.
- Zellkoordinaten beschriften.
- Objekte in Zellen platzieren.
- letzter Zug / selektiertes Feld hervorheben.
- Hit-Testing: Pixelposition → Brettkoordinate.
- Brettkoordinate → Zentrumspunkt.

## P6 – Charts

Diagramme sollen klein anfangen und später wachsen.

### Erste Charttypen

- Funktionsplot.
- Polyline-Plot.
- Scatterplot.
- Balkendiagramm.
- einfache Achsen.
- einfache Legende.

### Spätere Charttypen

- Histogramm.
- Boxplot.
- Heatmap.
- Suchbaum-/Graphvisualisierung.
- Bewertungsverlauf bei Game-AI.

## P7 – Renderer Backends

Nach SVG können konkrete Ausgabe- oder UI-Backends folgen.

| Backend | Zweck |
|---|---|
| Bitmap | Export von PNG/BMP für Dokumentation und Tests |
| Win32/GDI+ | einfache Windows-Demo ohne großes Framework |
| Direct2D | späteres performanteres Windows-Backend |
| Skia | plattformübergreifendes 2D-Rendering |
| Cairo | plattformübergreifendes 2D-Rendering, insbesondere Linux-nah |
| Terminal/Sixel | experimentell für TUI-nahe Visualisierung |
| HTML Canvas | späterer Web-/Dokumentations-Export |

## P8 – Demos

Demos sollen klein und verständlich bleiben.

- `demo_gomoku_board`
- `demo_function_plot`
- `demo_transforms`
- `demo_chess_board`
- `demo_svg_export`

Jede Demo sollte erklären, welches Konzept sie zeigt.

## P9 – Tests

### Testbereiche

- Geometrie.
- Koordinatentransformation.
- Bounds.
- Board-Mapping.
- SVG-Ausgabe.
- Chart-Skalierung.

### Testprinzip

Grafiktests sollten nicht nur Pixelvergleiche sein. Viele Tests können textbasiert oder modellbasiert erfolgen, z. B. durch Prüfung von SVG-Elementen, Koordinaten und Bounds.

## Spätere Ideen

- einfache Animationen.
- interaktive Werkzeuge.
- Export nach HTML Canvas.
- Scene-Inspector.
- kleine Designer-/Preview-Anwendung.
- Integration in SASD UI Toolkit oder SASD UI Platform.
