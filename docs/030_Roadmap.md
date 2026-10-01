# Roadmap

Diese Roadmap beschreibt eine sinnvolle Entwicklungsreihenfolge für das **SASD Graphics Toolkit**. Sie ist bewusst so aufgebaut, dass schnell sichtbare Ergebnisse entstehen, ohne die Architektur zu früh zu überfrachten.

## M0 – Repository Baseline

Ziel: Das Repository wirkt öffentlich verständlich und ist für Entwicklung vorbereitet.

### Ergebnis

- README mit Projektbeschreibung.
- Screenshot/Preview als SVG.
- Dokumentationsverzeichnis.
- Architekturüberblick.
- Feature-Katalog.
- AGENTS.md.
- Grundstruktur für `include/`, `src/` und `tests/`.

### Akzeptanzkriterien

- Ein Besucher versteht in unter zwei Minuten, was das Projekt werden soll.
- Die Abgrenzung zu GameWorks, Numerics und UI Toolkit ist dokumentiert.
- Die erste technische Richtung ist als modernes C++/CMake-Projekt erkennbar.

## M1 – Core Geometry

Ziel: Fundament für alle weiteren Grafikfunktionen schaffen.

### Umfang

- `point2d`
- `size2d`
- `vector2d`
- `rect2d`
- `line_segment2d`
- `bounds2d`
- einfache mathematische Hilfsfunktionen

### Akzeptanzkriterien

- Unit-Tests für alle Core-Typen.
- keine Abhängigkeit auf UI- oder Rendering-Frameworks.
- öffentliche Typen und Funktionen sind dokumentiert.

## M2 – Coordinate Mapping

Ziel: saubere Umrechnung zwischen Modell-, Welt- und Ausgabe-Koordinaten.

### Umfang

- Viewport.
- World-to-device Mapping.
- Skalierung.
- Translation.
- optionale Y-Achsen-Invertierung.
- Bounds-Clipping, zunächst einfach.

### Akzeptanzkriterien

- reproduzierbare Tests für typische Mapping-Fälle.
- dokumentiertes Beispiel für mathematischen Plot.
- dokumentiertes Beispiel für Brettkoordinate.

## M3 – Scene Model und Styles

Ziel: Zeichnungen als Modell beschreiben können.

### Umfang

- Scene.
- Layer.
- Shape-Primitive.
- StrokeStyle.
- FillStyle.
- TextStyle.
- einfache Z-Order.

### Akzeptanzkriterien

- eine Scene kann ohne Renderer erzeugt und geprüft werden.
- Styles sind unabhängig von Win32, Qt, GTK, Skia und Cairo.
- erste Beispielszene mit Grid, Linie und Text.

## M4 – SVG Renderer

Ziel: erster sichtbarer Output aus dem Scene Model.

### Umfang

- Export von Linien.
- Export von Rechtecken.
- Export von Kreisen.
- Export von Text.
- Export einfacher Pfade/Polylines.
- ViewBox-Unterstützung.

### Akzeptanzkriterien

- Demo erzeugt eine SVG-Datei.
- Tests prüfen zentrale SVG-Elemente.
- README-Screenshot kann perspektivisch aus dem Toolkit selbst erzeugt werden.

## M5 – Board Renderer

Ziel: Visualisierung für GameWorks Lab vorbereiten.

### Umfang

- generisches Grid.
- Go-Moku-Board.
- Schachbrett-Grunddarstellung.
- Feldbeschriftungen.
- Marker/Steine/Figuren-Platzhalter.
- Hit-Testing.

### Akzeptanzkriterien

- Go-Moku-Demo mit 19 × 19 Raster.
- letzter Zug kann hervorgehoben werden.
- Pixelposition kann in Brettkoordinate umgerechnet werden.
- SVG-Export funktioniert.

## M6 – Chart Basics

Ziel: einfache Visualisierung für Numerics/Math Toolkit.

### Umfang

- Achsen.
- Skalierung.
- Polyline-Serie.
- Scatter-Serie.
- einfache Legende.
- Funktionsplot-Demo.

### Akzeptanzkriterien

- Funktionswerte können visualisiert werden.
- Achsenbeschriftung ist einfach, aber brauchbar.
- keine numerischen Fachalgorithmen im Graphics Toolkit.

## M7 – Native oder dateibasierte Demo

Ziel: praktisches Testbett für Board, Chart und Export.

### Varianten

- zunächst dateibasierte CLI-Demo, die SVG-Dateien erzeugt.
- später optional native Demo mit Win32/Direct2D, Skia, Cairo oder Integration in SASD UI Toolkit.

### Akzeptanzkriterien

- Demo kann lokal gebaut und ausgeführt werden.
- Beispiel-SVG kann exportiert werden.
- keine Fachlogik im Rendering- oder UI-Code.

## M8 – Stabilisierung und erste Release-Vorbereitung

Ziel: erste nutzbare Vorabversion.

### Umfang

- API-Review.
- Dokumentation ergänzen.
- Beispiele aufräumen.
- CI einrichten.
- Lizenzentscheidung treffen.
- Versionierung festlegen.

### Akzeptanzkriterien

- Build und Tests laufen automatisiert.
- README spiegelt den tatsächlichen Stand wider.
- Release Notes beschreiben klar, was funktioniert und was nicht.

## Prioritätsregel

Wenn Unsicherheit entsteht, gilt:

> Erst eine konkrete, kleine Demo bauen. Dann abstrahieren.

Für den Anfang heißt das: **Go-Moku-Board + SVG-Export** ist wichtiger als ein perfektes allgemeines Grafikframework.
