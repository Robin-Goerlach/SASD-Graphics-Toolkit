# SASD Graphics Toolkit

> Modernes 2D-Grafik-, Visualisierungs- und Zeichenfundament für SASD-Projekte.

![SASD Graphics Toolkit Preview](assets/screenshots/sasd-graphics-toolkit-preview.svg)

## Zielbild

**SASD Graphics Toolkit** soll eine kleine, saubere und erweiterbare Grafikbibliothek werden, die als Unterbau für mehrere SASD-Projekte dienen kann:

- **SASD GameWorks Lab**: Brettspiel- und Kartenvisualisierung, Spielanalyse, Suchbäume, Bewertungsdiagramme.
- **SASD Numerics / Math Toolkit**: Funktionsplots, Diagramme, Koordinatensysteme, numerische Visualisierung.
- **SASD UI Platform / UI Toolkit**: wiederverwendbare Zeichenmodelle, Themes, Raster, einfache Controls und später Rendering-Backends.
- **Lehr- und Forschungsprojekte**: verständliche Beispiele für Grafik, Geometrie, Transformationen und algorithmische Visualisierung.

Das Projekt soll **kein schwergewichtiges Game-Engine-Framework** und **kein Ersatz für Qt, Avalonia oder WPF** werden. Es soll ein klar abgegrenzter, testbarer Grafik-Unterbau sein, der einfache Zeichnungen, Diagramme, Boards und Lernvisualisierungen zuverlässig möglich macht.

## Kernidee

Das Toolkit trennt konsequent zwischen:

```text
Grafisches Modell     -> Was soll gezeichnet werden?
Layout/Koordinaten    -> Wo und in welcher Skalierung?
Renderer              -> Wie wird es auf einer Zielplattform ausgegeben?
Anwendung             -> Warum wird es gezeichnet?
```

Dadurch kann dieselbe fachliche Grafik später auf verschiedene Ziele gerendert werden, zum Beispiel:

- WinForms / GDI+
- WPF / Win2D
- SkiaSharp
- SVG-Export
- Bitmap-Export
- später optional: Terminal/Sixel, HTML Canvas oder native Backends

## Geplante Feature-Gruppen

| Bereich | Geplante Funktionen |
|---|---|
| **Core Geometry** | Punkte, Linien, Rechtecke, Kreise, Polygone, Bounds, Vektoren |
| **Canvas Model** | Zeichenfläche, Layer, Viewport, Welt-/Bildschirmkoordinaten |
| **Rendering** | Linien, Flächen, Text, Symbole, Bilder, Stile, Themes |
| **Charts** | Achsen, Kurven, Scatterplots, Balken, einfache Legenden |
| **Boards & Grids** | Schachbrett, Go-Moku-Grid, Kartenbereiche, Zellraster, Hit-Testing |
| **Transforms** | Translation, Skalierung, Rotation, Mapping zwischen Koordinatensystemen |
| **Export** | SVG als erstes textbasiertes Austauschformat; Bitmap später |
| **Demos** | kleine, verständliche Beispielprogramme statt großer Demo-Monolithen |
| **Tests** | Geometrie-, Layout-, Transformations- und Exporttests |

## Abgrenzung

Das Toolkit soll **nicht** direkt Spiellogik, Schachregeln, Go-Moku-KI oder numerische Algorithmen enthalten. Diese gehören in eigene Projekte. Das Graphics Toolkit stellt nur die Visualisierung bereit.

```text
SASD.GameWorksLab        -> Spielregeln, KI, Spielzustände
SASD.Numerics.Core       -> Mathematik, Statistik, numerische Verfahren
SASD.Graphics.Toolkit    -> Darstellung, Koordinaten, Zeichenmodelle
SASD.UI.Platform         -> konkrete Desktop-Oberflächen und Bedienkonzepte
```

## Vorgeschlagene Architektur

```text
src/
├── Sasd.Graphics.Core
│   ├── Geometry
│   ├── Styling
│   ├── SceneGraph
│   ├── Coordinates
│   └── Export
├── Sasd.Graphics.Rendering.Svg
├── Sasd.Graphics.Rendering.WinForms
├── Sasd.Graphics.Charts
├── Sasd.Graphics.Boards
└── Sasd.Graphics.DemoApp

tests/
├── Sasd.Graphics.Core.Tests
├── Sasd.Graphics.Rendering.Svg.Tests
├── Sasd.Graphics.Charts.Tests
└── Sasd.Graphics.Boards.Tests
```

## Erste sinnvolle Demo

Als erste Demo bietet sich ein **Go-Moku-Board** an:

- 19 × 19 Raster
- Steine als einfache Kreise
- letzter Zug hervorgehoben
- Koordinaten A–S / 1–19
- Hit-Testing von Mausposition auf Brettposition
- Export als SVG

Diese Demo ist klein genug für einen schnellen Start, aber fachlich nützlich für das spätere **SASD GameWorks Lab**.

## Roadmap

| Meilenstein | Ergebnis |
|---|---|
| **M0 – Repository Baseline** | README, Screenshot, Dokumentation, Struktur, Entwicklungsregeln |
| **M1 – Core Geometry** | Punkte, Größen, Rechtecke, Linien, Bounds, Transformationen |
| **M2 – Scene & Style Model** | Primitive, Zeichenbefehle, Farben, Linienarten, Layer |
| **M3 – SVG Renderer** | reproduzierbarer Export ohne native UI-Abhängigkeit |
| **M4 – Board Renderer** | Raster, Brettspiele, Koordinaten, Hit-Testing |
| **M5 – Chart Basics** | einfache Kurven-, Punkt- und Achsendiagramme |
| **M6 – WinForms Demo App** | interaktive Demo mit Board, Chart und Export |

## Dokumentation

| Dokument | Zweck |
|---|---|
| [docs/000_Project_Overview.md](docs/000_Project_Overview.md) | Projektidee, Zielgruppen, Produktgrenzen |
| [docs/010_Feature_Catalog.md](docs/010_Feature_Catalog.md) | Feature-Liste und Prioritäten |
| [docs/020_Architecture.md](docs/020_Architecture.md) | Architektur, Layering, Designentscheidungen |
| [docs/030_Roadmap.md](docs/030_Roadmap.md) | Entwicklungsphasen und sinnvolle Reihenfolge |
| [docs/040_Integration_GameWorks_Numerics.md](docs/040_Integration_GameWorks_Numerics.md) | Zusammenspiel mit GameWorks und Numerics |
| [AGENTS.md](AGENTS.md) | Arbeitsregeln für Codex/AI-gestützte Entwicklung |

## Entwicklungsprinzipien

1. **Klein anfangen, sauber trennen.** Erst Core + SVG, dann UI-Backends.
2. **Keine Framework-Vermischung.** Core bleibt frei von WinForms/WPF/Skia-Abhängigkeiten.
3. **Testbare Geometrie.** Berechnungen müssen ohne UI getestet werden können.
4. **Dokumentation parallel zum Code.** Jede größere Entscheidung bekommt eine kurze Begründung.
5. **Beispiele vor Abstraktion.** Abstraktionen entstehen aus konkreten Demos, nicht umgekehrt.

## Status

Aktueller Stand: **Repository-Baseline / Konzeptphase**.

Noch nicht vorhanden:

- produktiver Code
- NuGet-Pakete
- CI/CD
- Lizenzentscheidung
- stabiler API-Vertrag

## Lizenz

Noch offen. Vor der ersten öffentlichen Release-Version sollte bewusst entschieden werden, ob das Projekt MIT, Apache-2.0, LGPL, MPL oder AGPL nutzen soll.

## Leitmotiv

> Zeichne nicht nur Pixel. Zeichne Modelle, die man verstehen, testen und wiederverwenden kann.
