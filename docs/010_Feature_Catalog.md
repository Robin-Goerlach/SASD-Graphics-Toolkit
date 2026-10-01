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

- `Point2D`
- `Size2D`
- `Vector2D`
- `Rectangle2D`
- `LineSegment2D`
- `Circle2D`
- `Polygon2D`
- `Bounds2D`

### Operationen

- Distanzberechnung.
- Bounds-Berechnung.
- Schnitt- und Enthält-Prüfungen, zunächst nur einfache Fälle.
- Normalisierung von Rechtecken.
- Mapping von Weltkoordinaten auf Bildschirmkoordinaten.

## P2 – Styling

Stile beschreiben die Darstellung, nicht die Fachlogik.

- Farben.
- Linienbreite.
- Linienart.
- Füllung.
- Textstil.
- Symbolstil.
- Themes.

Wichtig: Der Core sollte eigene einfache Stilmodelle besitzen und nicht direkt `System.Drawing.Color`, WPF-Brushes oder Skia-Typen verwenden.

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

Nach SVG können konkrete UI-Backends folgen.

| Backend | Zweck |
|---|---|
| WinForms | einfache Demo-App, schnelle Integration in bestehende Windows-Projekte |
| WPF | bessere Vektor-/Layoutintegration, spätere Desktop-Demos |
| SkiaSharp | plattformübergreifendes 2D-Rendering |
| Bitmap | Export von PNG/JPEG für Doku und Tests |
| Terminal/Sixel | experimentell für TUI-nahe Visualisierung |

## P8 – Demos

Demos sollen klein und verständlich bleiben.

- `Demo_GomokuBoard`
- `Demo_FunctionPlot`
- `Demo_Transforms`
- `Demo_ChessBoard`
- `Demo_SvgExport`

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
- Integration in SASD UI Platform.
