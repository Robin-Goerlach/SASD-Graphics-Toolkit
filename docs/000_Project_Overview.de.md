# SASD Graphics Toolkit – Projektüberblick

## Kurzbeschreibung

**SASD Graphics Toolkit** ist als moderner 2D-Grafik-Unterbau für SASD-Projekte geplant. Der Fokus liegt nicht auf einer Endanwender-Anwendung, sondern auf wiederverwendbaren Modellen, Zeichenoperationen, Koordinatensystemen und Renderern.

Das Toolkit soll Projekte wie **SASD GameWorks Lab**, **SASD Numerics / Math Toolkit**, **SASD UI Toolkit** und spätere Lern- oder Forschungswerkzeuge unterstützen.

## Warum dieses Projekt existiert

Mehrere SASD-Projekte benötigen ähnliche Visualisierungsfunktionen:

- Raster und Bretter für klassische Spiele,
- Funktionsplots und Diagramme für Numerik und Statistik,
- kompakte 2D-Zeichnungen für Dokumentation und Analyse,
- exportierbare Visualisierungen, besonders SVG,
- klare Trennung zwischen Fachmodell und Rendering.

Ein gemeinsames Graphics Toolkit vermeidet, dass diese Konzepte in mehreren Repositories mehrfach entstehen.

## Zielgruppen

- Entwickler, die testbare Grafikmodelle ohne Bindung an ein konkretes UI-Framework benötigen.
- Leser und Lernende, die verständliche Beispiele für Geometrie, Mapping und Rendering suchen.
- SASD-Projekte, die Bretter, Charts, Diagramme oder visuelle Debug-Ausgaben benötigen.

## Im Umfang enthalten

- 2D-Geometrieprimitive.
- Koordinaten-Mapping und Transformationen.
- Szenen- und Layer-Modelle.
- SVG als erstes Renderer-/Exportziel.
- Bretter, Raster und einfache Charts.
- Kleine Demos und Tests.

## Nicht im Umfang enthalten

- vollständige Game Engine.
- vollständiges GUI-Framework.
- Spielregeln oder KI-Algorithmen.
- numerische Algorithmen, die in SASD Numerics gehören.
- Ersatz für Qt, GTK, wxWidgets, Skia oder Cairo.

## Leitentscheidungen

1. Der Core bleibt frei von UI-Framework-Abhängigkeiten.
2. SVG kommt früh, weil es textbasiert, testbar und dokumentationsfreundlich ist.
3. Echte Demos treiben die Abstraktionen.
4. Geometrie- und Mapping-Logik bleibt ohne Display testbar.
5. Dokumentation bleibt nah an Implementierungsentscheidungen.

## Erstes erwartetes Ergebnis

Der erste sinnvolle Meilenstein sollte eine kleine C++20/CMake-Basis mit Core-Geometrie, einfachem SVG-Exportpfad, Unit-Tests und einer kleinen visuellen Demo liefern.
