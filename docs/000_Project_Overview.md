# SASD Graphics Toolkit – Project Overview

## Kurzbeschreibung

**SASD Graphics Toolkit** ist als moderner 2D-Grafik-Unterbau für SASD-Projekte gedacht. Der Schwerpunkt liegt nicht auf einer fertigen Endanwender-Anwendung, sondern auf wiederverwendbaren Modellen, Zeichenoperationen, Koordinatensystemen und Renderern.

Das Toolkit soll später in Projekten wie **SASD GameWorks Lab**, **SASD Numerics / Math Toolkit**, **SASD UI Platform** und weiteren Lern- oder Forschungsanwendungen eingesetzt werden.

## Warum dieses Projekt?

Mehrere SASD-Projekte benötigen ähnliche grafische Grundfunktionen:

- Raster und Bretter für klassische Spiele.
- Funktionsplots und Diagramme für Numerik und Statistik.
- einfache 2D-Zeichnungen für Dokumentation, Analyse und Demos.
- exportierbare Visualisierungen, insbesondere SVG.
- saubere Trennung zwischen Fachmodell und Darstellung.

Ohne gemeinsamen Unterbau würden diese Funktionen in mehreren Repositories mehrfach entstehen. Das Graphics Toolkit soll diese Wiederholung vermeiden, ohne sofort ein übergroßes Framework zu werden.

## Zielgruppen

### Entwickler

Entwickler sollen einfache, testbare Grafikmodelle verwenden können, ohne sofort an WinForms, WPF, SkiaSharp oder ein anderes konkretes Backend gebunden zu sein.

### Lernende und Leser der Dokumentation

Die Bibliothek soll verständlich aufgebaut sein. Geometrie, Koordinaten, Transformationen, Layer und Rendering sollen nachvollziehbar dokumentiert werden.

### SASD-Projekte

Andere SASD-Projekte sollen das Toolkit gezielt als Unterbau nutzen können, sobald konkrete Funktionen stabil genug sind.

## Produktgrenzen

### Das Projekt soll leisten

- 2D-Grundgeometrie bereitstellen.
- Zeichenmodelle und einfache Szenen beschreiben.
- Koordinatensysteme und Transformationen abbilden.
- SVG als erstes Exportformat unterstützen.
- Boards, Grids und einfache Charts ermöglichen.
- Beispiele und Tests liefern.

### Das Projekt soll bewusst nicht leisten

- keine komplette Game Engine.
- kein vollwertiges GUI-Framework.
- kein Ersatz für WPF, WinForms, Avalonia, Qt oder Skia.
- keine Spielregeln oder Spiel-KI.
- keine numerischen Algorithmen, die besser in SASD Numerics gehören.

## Leitende Entscheidungen

1. **Core zuerst:** Die Kernbibliothek bleibt frei von UI-Framework-Abhängigkeiten.
2. **SVG früh:** SVG ist ideal als erstes Ziel, weil es textbasiert, testbar und dokumentationsfreundlich ist.
3. **Demos als Treiber:** Abstraktionen entstehen aus konkreten Beispielen wie Go-Moku-Board, Koordinatensystem und Funktionsplot.
4. **Testbarkeit:** Geometrie- und Transformationslogik muss ohne UI getestet werden können.
5. **Dokumentation parallel:** Jedes größere Konzept erhält eine kurze Erklärung und mindestens ein Beispiel.

## Erwartetes erstes Ergebnis

Nach der ersten Implementierungsphase sollte das Repository mindestens enthalten:

- eine Solution-Struktur,
- `Sasd.Graphics.Core`,
- grundlegende Geometrietypen,
- einen einfachen SVG-Renderer,
- Unit-Tests,
- eine kleine Demo-Ausgabe als SVG,
- Dokumentation zur Architektur.

## Langfristige Vision

Langfristig kann das Toolkit zur **SASD Graphics Toolbox** ausgebaut werden: ein kleines, robustes Fundament für Zeichnungen, Diagramme, technische Visualisierungen, Spielbretter und Lehrbeispiele.
