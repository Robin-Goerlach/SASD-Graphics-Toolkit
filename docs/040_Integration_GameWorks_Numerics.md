# Integration mit GameWorks Lab und Numerics

## Ausgangslage

Das SASD Graphics Toolkit soll nicht isoliert entstehen. Es ist als Unterbau für mehrere SASD-Projekte gedacht, insbesondere:

- **SASD GameWorks Lab**
- **SASD Numerics / Math Toolkit**
- **SASD UI Platform / UI Toolkit**

Die zentrale Frage lautet: Was gehört in welches Projekt?

## Grundsatz

> Graphics visualisiert. Numerics rechnet. GameWorks spielt. UI bedient.

Diese Trennung ist wichtig, damit keine schwer wartbaren Abhängigkeiten entstehen.

## Abgrenzung zu SASD GameWorks Lab

### Gehört ins GameWorks Lab

- Spielregeln.
- Spielzustände.
- erlaubte Züge.
- KI-Spieler.
- Bewertungsfunktionen.
- Suchalgorithmen.
- Partieprotokolle.

### Gehört ins Graphics Toolkit

- Brettdarstellung.
- Rasterdarstellung.
- Zeichnen von Steinen, Figuren oder Karten.
- Markierung eines Feldes.
- Koordinatenbeschriftung.
- Hit-Testing von Mausposition auf Brettfeld.
- Export einer Brettstellung als SVG.

### Beispiel Go-Moku

```text
GameWorks:
- BoardState 19x19
- Move(row, column, player)
- Win detection
- AI evaluation

Graphics Toolkit:
- GridRenderer
- StoneShape
- BoardCoordinateLabelRenderer
- LastMoveHighlight
- BoardHitTester
```

## Abgrenzung zu SASD Numerics / Math Toolkit

### Gehört in Numerics

- lineare Algebra.
- Statistik.
- Interpolation.
- Approximation.
- Optimierung.
- numerische Integration.
- Regression.
- Datenanalyse.

### Gehört ins Graphics Toolkit

- Achsen.
- Plot-Fläche.
- Datenserien als Darstellung.
- Skalierung in Bildschirmkoordinaten.
- Legenden.
- SVG-/Bitmap-Export.

### Beispiel Funktionsplot

```text
Numerics:
- berechnet f(x)
- erzeugt Datenpunkte
- analysiert Nullstellen oder Extrema

Graphics Toolkit:
- zeichnet Achsen
- mappt Werte auf Pixel/SVG-Koordinaten
- zeichnet Kurve und Marker
```

## Abgrenzung zu SASD UI Platform / UI Toolkit

### Gehört in UI Platform / UI Toolkit

- Fenster.
- Menüs.
- Toolbars.
- Bedienkonzepte.
- Formulare.
- Dialoge.
- Desktop-Komponenten.

### Gehört ins Graphics Toolkit

- Zeichenmodell.
- Renderer.
- Zeichenprimitive.
- Koordinatenlogik.
- Export.

Die UI kann Graphics verwenden, aber Graphics sollte nicht von konkreten UI-Projekten abhängig sein.

## Repository-Strategie

Für den Start ist es sinnvoll, das Graphics Toolkit als eigenständiges Repository zu führen, aber die ersten Features aus konkreten Nachbarprojekten abzuleiten.

### Empfohlener Treiber

1. Go-Moku-Board aus GameWorks Lab.
2. Funktionsplot aus Numerics/Math Toolkit.
3. einfache Demo-App aus UI Platform.

Diese Reihenfolge verhindert, dass das Toolkit zu theoretisch wird.

## Umgang mit Doppelentwicklung

Nicht jede kleine Hilfsfunktion muss sofort in ein gemeinsames Projekt extrahiert werden.

### Im Fachprojekt lassen

- einmalige Hilfsfunktionen.
- stark fachliche Logik.
- experimenteller Code.
- Demo-spezifische Sonderfälle.

### In Graphics Toolkit übernehmen

- mehrfach benötigte Geometrietypen.
- wiederverwendbare Koordinatenmodelle.
- generische Renderer.
- Board-/Grid-Darstellung.
- Exportfunktionen.

## Empfohlene erste Schnittstelle zu GameWorks

GameWorks sollte keine Graphics-Typen in seine Kernlogik übernehmen müssen. Stattdessen kann ein Adapter die fachlichen Zustände übersetzen.

```text
GameWorks BoardState
    -> GameWorksGraphicsAdapter
        -> Graphics Scene
            -> SvgRenderer / WinFormsRenderer
```

So bleibt die Spiellogik unabhängig von der Darstellung.

## Empfohlene erste Schnittstelle zu Numerics

Numerics liefert Daten, Graphics zeichnet sie.

```text
Numerics Result
    -> PlotDataSeries
        -> ChartSceneBuilder
            -> SvgRenderer
```

Auch hier gilt: Numerics sollte nicht direkt wissen müssen, ob eine Kurve nach SVG oder WinForms gerendert wird.

## Entscheidung für den Projektstart

Das Graphics Toolkit sollte zuerst genau zwei reale Szenarien unterstützen:

1. **Go-Moku-Board als SVG.**
2. **einfacher Funktionsplot als SVG.**

Wenn diese beiden Szenarien sauber funktionieren, ist der Kern vermutlich richtig geschnitten.
