# Architecture Overview

## Architekturziel

Die Architektur des **SASD Graphics Toolkit** soll eine klare Trennung zwischen Modell, Koordinatenlogik, Styling und konkretem Rendering ermöglichen.

Das wichtigste Ziel lautet:

> Der fachliche Grafik-Core darf nicht wissen, ob später nach SVG, WinForms, WPF, SkiaSharp oder Bitmap gerendert wird.

## Layer-Modell

```text
Application / Demo
    |
    v
Domain-specific Visualizers
    |        Beispiel: GoMokuBoardVisualizer, FunctionPlotVisualizer
    v
Scene Model
    |        Primitive, Layer, Styles, Text, Shapes
    v
Coordinate & Layout Core
    |        Viewport, Bounds, Transformations, Hit-Testing
    v
Renderer Abstraction
    |        IRenderer, RenderTarget, RenderContext
    v
Concrete Renderer
             SvgRenderer, WinFormsRenderer, WpfRenderer, SkiaRenderer
```

## Vorgeschlagene Projekte

```text
src/
├── Sasd.Graphics.Core
├── Sasd.Graphics.Rendering.Svg
├── Sasd.Graphics.Boards
├── Sasd.Graphics.Charts
├── Sasd.Graphics.Rendering.WinForms
└── Sasd.Graphics.DemoApp
```

## Sasd.Graphics.Core

Der Core ist die wichtigste Schicht. Er enthält keine UI-Abhängigkeit.

### Verantwortlichkeiten

- Geometrietypen.
- Stylemodelle.
- Zeichenprimitive.
- Layer und Scene Graph.
- Koordinatentransformationen.
- Bounds-Berechnung.
- Renderer-Abstraktionen.

### Nicht im Core

- `System.Windows.Forms`.
- WPF-Typen.
- SkiaSharp-Typen.
- konkrete Dateidialoge.
- Spiellogik.
- numerische Fachalgorithmen.

## Scene Model

Das Scene Model beschreibt die gewünschte Darstellung.

Beispiel:

```text
Scene
├── Layer: Grid
│   ├── Line
│   ├── Line
│   └── Text
├── Layer: Data
│   ├── Polyline
│   └── CircleMarker
└── Layer: Overlay
    └── SelectionRectangle
```

Eine Szene ist ein transportables Modell. Renderer übersetzen dieses Modell in ein konkretes Ziel.

## Renderer-Abstraktion

Eine spätere Minimalform könnte so aussehen:

```csharp
public interface IGraphicsRenderer
{
    void Render(Scene scene, RenderTarget target, RenderOptions options);
}
```

Für den Start kann eine einfachere API genügen. Wichtig ist nur, dass der Renderer austauschbar bleibt.

## Koordinatensysteme

Das Toolkit sollte mindestens drei Koordinatenebenen unterscheiden:

| Ebene | Bedeutung |
|---|---|
| Model Coordinates | Fachliche Koordinaten, z. B. Brettfeld oder mathematischer Wert |
| World Coordinates | kontinuierlicher Grafikraum |
| Device Coordinates | Pixel, SVG-Einheiten oder Backend-Koordinaten |

Diese Trennung verhindert, dass UI-Details in die Fachlogik rutschen.

## Boards und Hit-Testing

Boards sind ein wichtiger Spezialfall.

Ein Board-Renderer sollte können:

- Zellgröße berechnen.
- Rand und Beschriftung berücksichtigen.
- Feldkoordinate in Mittelpunkt umrechnen.
- Maus-/Pixelposition in Feldkoordinate umrechnen.
- ungültige Positionen sauber ablehnen.

Beispiel:

```text
screen point (312, 188)
    -> board local point (172, 94)
    -> cell coordinate (H, 10)
```

## Charts

Charts sollten nicht sofort als großes Framework entstehen. Für den Anfang reicht:

- Achsenmodell.
- Datenserie.
- Skalierung.
- Polyline-Ausgabe.
- optionale Marker.

Statistische oder numerische Berechnungen gehören nicht in Charts, sondern in SASD Numerics. Charts visualisieren Ergebnisse.

## Fehlervermeidung

### Gefahr: zu früh zu allgemein

Das Projekt darf nicht mit einem riesigen abstrakten Scene Graph starten, der noch keine konkrete Demo bedienen kann.

Gegenmaßnahme:

- erst Go-Moku-Board und SVG-Export,
- dann Funktionsplot,
- danach gemeinsame Abstraktionen festigen.

### Gefahr: Backend-Vermischung

Wenn im Core direkt WinForms- oder WPF-Typen auftauchen, wird die Bibliothek schwer wiederverwendbar.

Gegenmaßnahme:

- eigene Core-Typen,
- Adapter in separaten Projekten,
- klare Projektabhängigkeiten.

### Gefahr: GameWorks-Logik im Graphics Toolkit

Ein Go-Moku-Board darf visualisiert werden, aber Gewinnprüfung und KI gehören nicht hierher.

Gegenmaßnahme:

- `Boards` kennt Felder und Steine als Darstellung,
- `GameWorks` kennt Regeln, Züge und Bewertung.

## Empfohlene erste technische Entscheidung

Als erstes produktives Backend sollte **SVG** umgesetzt werden. Dadurch entsteht schnell sichtbarer Output, ohne eine UI-Anwendung bauen zu müssen. Außerdem kann das Ergebnis direkt in README, Dokumentation und Tests verwendet werden.
