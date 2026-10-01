# Architecture Overview

## Architekturziel

Die Architektur des **SASD Graphics Toolkit** soll eine klare Trennung zwischen Modell, Koordinatenlogik, Styling und konkretem Rendering ermöglichen.

Das wichtigste Ziel lautet:

> Der fachliche Grafik-Core darf nicht wissen, ob später nach SVG, Win32/GDI+, Direct2D, Skia, Cairo, Terminal/Sixel oder Bitmap gerendert wird.

## Layer-Modell

```text
Application / Demo
    |
    v
Domain-specific Visualizers
    |        Beispiel: GomokuBoardVisualizer, FunctionPlotVisualizer
    v
Scene Model
    |        Primitive, Layer, Styles, Text, Shapes
    v
Coordinate & Layout Core
    |        Viewport, Bounds, Transformations, Hit-Testing
    v
Renderer Abstraction
    |        Renderer, RenderTarget, RenderContext
    v
Concrete Renderer
             SvgRenderer, BitmapRenderer, Win32Renderer, SkiaRenderer, CairoRenderer
```

## Vorgeschlagene Projektstruktur

```text
include/
└── sasd/graphics/
    ├── geometry/
    ├── styling/
    ├── scene/
    ├── coordinates/
    ├── export/
    ├── boards/
    └── charts/

src/
├── core/
├── rendering_svg/
├── boards/
├── charts/
└── demo/

tests/
├── core/
├── rendering_svg/
├── boards/
└── charts/
```

## Core

Der Core ist die wichtigste Schicht. Er enthält keine Abhängigkeit auf konkrete UI- oder Rendering-Frameworks.

### Verantwortlichkeiten

- Geometrietypen.
- Stylemodelle.
- Zeichenprimitive.
- Layer und Scene Graph.
- Koordinatentransformationen.
- Bounds-Berechnung.
- Renderer-Abstraktionen.

### Nicht im Core

- Win32/GDI+-Typen.
- Direct2D-Typen.
- Qt-/GTK-Typen.
- Skia-/Cairo-Typen.
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

```cpp
namespace sasd::graphics
{
    class renderer
    {
    public:
        virtual ~renderer() = default;
        virtual void render(const scene& scene, const render_options& options) = 0;
    };
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

## CMake-Zielbild

Eine mögliche Zielstruktur der CMake-Targets:

```text
sasd_graphics_core
sasd_graphics_rendering_svg
sasd_graphics_boards
sasd_graphics_charts
sasd_graphics_demo
```

Die Core-Bibliothek sollte zuerst auch ohne optionale Renderer baubar sein.

## Fehlervermeidung

### Gefahr: zu früh zu allgemein

Das Projekt darf nicht mit einem riesigen abstrakten Scene Graph starten, der noch keine konkrete Demo bedienen kann.

Gegenmaßnahme:

- erst Go-Moku-Board und SVG-Export,
- dann Funktionsplot,
- danach gemeinsame Abstraktionen festigen.

### Gefahr: Backend-Vermischung

Wenn im Core direkt Win32-, Qt-, GTK-, Skia- oder Cairo-Typen auftauchen, wird die Bibliothek schwer wiederverwendbar.

Gegenmaßnahme:

- eigene Core-Typen,
- Adapter in separaten Modulen,
- klare Projektabhängigkeiten.

### Gefahr: GameWorks-Logik im Graphics Toolkit

Ein Go-Moku-Board darf visualisiert werden, aber Gewinnprüfung und KI gehören nicht hierher.

Gegenmaßnahme:

- `boards` kennt Felder und Steine als Darstellung,
- `GameWorks` kennt Regeln, Züge und Bewertung.

## Empfohlene erste technische Entscheidung

Als erstes produktives Backend sollte **SVG** umgesetzt werden. Dadurch entsteht schnell sichtbarer Output, ohne eine UI-Anwendung bauen zu müssen. Außerdem kann das Ergebnis direkt in README, Dokumentation und Tests verwendet werden.
