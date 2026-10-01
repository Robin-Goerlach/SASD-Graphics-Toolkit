# Architekturüberblick

## Ziel

Die Architektur des **SASD Graphics Toolkit** soll fachliche Visualisierung, Geometrie, Styling und konkretes Rendering klar trennen.

Die wichtigste Regel lautet:

> Der Grafik-Core darf nicht wissen, ob eine Szene nach SVG, Bitmap, Win32, Direct2D, Skia, Cairo oder ein späteres UI-Backend gerendert wird.

## Layer-Modell

```text
Application / Demo
    |
    v
Domain-specific Visualizers
    |
    v
Scene Model
    |
    v
Geometry + Coordinates + Styles
    |
    v
Renderer Backend
```

## Geplante Module

| Modul | Verantwortung |
|---|---|
| `sasd::graphics::geometry` | Punkte, Vektoren, Rechtecke, Bounds, Linien, Kreise |
| `sasd::graphics::coordinates` | Viewports, World-to-device Mapping, Transformationen |
| `sasd::graphics::style` | Farben, Linien, Füllungen, Textstile, Themes |
| `sasd::graphics::scene` | Layer, Shapes, Text, IDs, Z-Order |
| `sasd::graphics::rendering::svg` | SVG-Export |
| `sasd::graphics::boards` | Raster, Brettkoordinaten, Hit-Testing |
| `sasd::graphics::charts` | Achsen, Serien, einfache Plots |

## Grundprinzipien

1. Der Core ist unabhängig von UI-Frameworks.
2. Renderer übersetzen das Scene Model in konkrete Ausgabe.
3. Fachliche Visualizer liegen außerhalb des Renderers.
4. Tests prüfen bevorzugt Geometrie und exportierten Text.
5. Demos treiben die API-Form, bevor die Bibliothek zu abstrakt wird.

## Erstes Backend: SVG

SVG ist das bevorzugte erste Backend, weil es textbasiert, reviewbar, gut testbar und für README-Dateien sowie Dokumentation nützlich ist.

## Spätere Backends

Spätere Renderer-Backends können Bitmap-Export, Win32/GDI+, Direct2D, Skia, Cairo, HTML Canvas oder terminalnahe Experimente umfassen. Sie sollten erst ergänzt werden, wenn Scene Model und Koordinaten-Mapping ausreichend stabil sind.
