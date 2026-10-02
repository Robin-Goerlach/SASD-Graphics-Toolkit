# Zusätzlicher Projektkontext aus der GameWorks-Diskussion

> **Dokumenttyp:** nicht-normativer Projektkontext
>
> **Standardsprache:** Englisch. Maßgebliche Standardfassung: [090_Conversation_Context.md](../en/090_Conversation_Context.md)
>
> Dieses Dokument bewahrt Entscheidungen, Ideen, Abgrenzungen, Referenzprodukte und die visuelle Richtung für das **SASD Graphics Toolkit**, die in einer breiteren Diskussion entstanden sind, deren Ausgangspunkt ursprünglich das **SASD GameWorks Lab** war. Es wurde angelegt, weil mehrere dieser Punkte für das Graphics Toolkit selbst wichtig sind, für GameWorks aber nur mittelbar relevant.
>
> Normativ bleiben Projektüberblick, Architektur, Feature-Katalog, Roadmap und zukünftige ADRs. Falls dieses Kontextdokument einer neueren dedizierten Projektdokumentation oder implementiertem Code widerspricht, hat die neuere dedizierte Quelle Vorrang.

## Aktuelle Regeln nach dem Repository-Umbau

Dokument-ID: GFX-DOC-CONTEXT. Die folgenden Abschnitte bewahren die historische Diskussion.
Die aktuelle [Architektur](020_Architecture.md) ersetzt ältere Aussagen zur ausschließlichen
C++-Ausrichtung, flachen Dokumentation und Geometriezuständigkeit: C++ kommt zuerst,
C#/.NET ist gleichrangig geplant, Sprachordner sind maßgeblich und die kleine Math-Grenze
steht im vorgeschlagenen ADR-GFX-003. Die [Unterstützungsmatrix](070_Language_Support.md)
zeigt den tatsächlichen Implementierungsstand.

## 1. Warum das Graphics Toolkit entstanden ist

Die breitere GameWorks-Diskussion begann mit der Idee, das historische Turbo-GameWorks-Konzept modern neu zu interpretieren. GameWorks benötigt grafische Bausteine für Spielbretter, Analysen, Diagramme und Lernbeispiele. Gleichzeitig benötigen andere SASD-Projekte viele derselben grundlegenden Funktionen.

Daraus entstand eine zentrale Entscheidung: Gemeinsame Grafikfunktionalität soll nicht in jeder Anwendung erneut implementiert werden. Stattdessen soll das **SASD Graphics Toolkit als eigenständige wiederverwendbare Bibliothek** GameWorks und weitere SASD-Projekte versorgen.

Dasselbe Prinzip gilt für numerische Funktionalität: GameWorks kann sowohl ein Graphics Toolkit als auch ein Numerics/Math Toolkit verwenden, soll aber keines von beiden besitzen.

## 2. Zentrale Architekturentscheidung

Die bevorzugte langfristige Struktur ist konzeptionell:

```text
SASD GameWorks Lab
    |
    +--> SASD Graphics Toolkit
    |
    +--> SASD Numerics / Math Toolkit

Weitere SASD-Anwendungen
    |
    +--> SASD Graphics Toolkit
    +--> SASD Numerics / Math Toolkit
```

Die Bibliotheken bleiben unabhängig nutzbar. GameWorks ist ein wichtiger Anforderungstreiber, aber nicht Eigentümer der Abstraktionen.

Als praktische Regel wurde diskutiert:

> Eine wiederverwendbare Abstraktion wird dann herausgelöst, wenn sie klar generisch ist oder dieselbe Funktionalität sonst mehrfach implementiert würde.

Damit sollen zwei Extreme vermieden werden:

- Geometrie, Plotting, Board-Rendering und Exportlogik in jeder Anwendung zu duplizieren;
- ein riesiges abstraktes Grafikframework zu bauen, bevor eine reale Anwendung es benötigt.

Die Implementierung soll daher **anwendungsgetrieben, aber architektonisch unabhängig** erfolgen.

## 3. Aktuelle Technologierichtung

In einer frühen Konzeptphase wurden kurz C#-orientierte Grafikmodule mit WinForms/WPF-Adaptern angesprochen, weil die erste GameWorks-Anwendungsidee als .NET-Desktop-Anwendung gedacht war. Für dieses Repository gilt das inzwischen als überholte Explorationsphase.

Die später festgelegte Richtung für das eigenständige Repository lautet:

- **C++20** als Implementierungssprache;
- **CMake** als Buildsystem;
- ein frameworkneutraler Grafik-Core;
- klar abgegrenzte Renderer-Backends;
- englische Dokumentation als Standard mit deutschen Begleitfassungen.

WinForms/WPF können im größeren SASD-Ökosystem weiterhin Konsumenten über Adapter oder Bindings sein, dürfen aber das Core-Modell des Graphics Toolkit nicht bestimmen.

## 4. Trennung der Verantwortlichkeiten

Ein mehrfach betontes Designprinzip ist die Trennung von vier Aspekten:

```text
Grafikmodell        -> was soll gezeichnet werden?
Layout/Koordinaten  -> wo und in welcher Skalierung?
Renderer-Backend    -> wie wird es ausgegeben oder angezeigt?
Anwendungslogik     -> warum wird es gezeichnet?
```

Daraus ergeben sich folgende Projektgrenzen:

### SASD Graphics Toolkit besitzt

- 2D-Geometrie und Bounds;
- Koordinatenabbildung und Viewports;
- grafische Szenenbeschreibungen;
- abstrakte Styles und Themes;
- wiederverwendbare Board-/Grid-Visualisierung;
- Chart- und Plot-Primitiven;
- Renderer-/Export-Adapter;
- Hit-Testing und Koordinatenumrechnung, soweit dies grafische Aufgaben sind;
- Beispiele und visualisierungsbezogene Tests.

### SASD GameWorks Lab besitzt

- Spielregeln;
- Erzeugung legaler Züge;
- Spielzustände;
- Spiel-KI und Suchstrategien;
- Schach-, Go-Moku-, Bridge- oder andere Domänenlogik;
- fachliche Interpretation von Spielanalysen.

### SASD Numerics / Math Toolkit besitzt

- mathematische und numerische Algorithmen;
- Statistik und numerische Verfahren;
- numerische Optimierung;
- mathematische Datenaufbereitung;
- fachliche Berechnungen hinter Plots.

### SASD UI Toolkit / UI Platform besitzt

- Interaktions- und Widget-Konzepte;
- Controls, Menüs, Fokus, Command Handling und höheres UI-Verhalten;
- native UI-Integration jenseits der Rendering-Verantwortung des Graphics Toolkit.

Ziel ist, zirkuläre Zuständigkeiten und versteckte Kopplung zwischen den Projekten zu vermeiden.

## 5. In der Diskussion identifizierte Feature-Bereiche

### 5.1 Core Geometry

Als erste wiederverwendbare Typen wurden genannt:

- `point2d`
- `size2d`
- `vector2d`
- `rect2d`
- `bounds2d`
- `line_segment2d`
- `circle2d`
- `polygon2d`

Relevante Operationen sind Distanz, Enthält-Prüfungen, Bounds-Berechnung, einfache Schnittprüfungen, Rechtecknormalisierung und Abbildung zwischen Koordinatensystemen.

### 5.2 Koordinatensysteme und Transformationen

Das Toolkit soll Modell-/Weltkoordinaten klar von Ausgabe-/Device-Koordinaten unterscheiden.

Diskutiert wurden:

- Viewports;
- Translation;
- Skalierung;
- Rotation, wo sinnvoll;
- optionale Y-Achsen-Invertierung;
- World-to-Device und Device-to-World Mapping;
- einfaches Clipping und Bounds-Handling;
- Brettkoordinate zu Device-Koordinate;
- Device-Position zu Brettzelle bzw. Brettschnittpunkt per Hit-Testing.

### 5.3 Scene Model

Eine Szene soll beschreiben, **was** gezeichnet wird, ohne die konkrete Rendering-Technologie zu kennen.

Mögliche Konzepte:

- Scene;
- Layer;
- Group;
- Z-Order;
- Shape-Primitiven;
- stabile IDs für Hit-Testing und Debugging;
- Linie, Rechteck, Kreis/Ellipse, Polygon, Pfad, Text;
- später Bildreferenzen.

### 5.4 Styling

Styles sollen rendererneutral sein und nicht auf konkrete Typen aus Win32, Qt, Skia, Cairo, WPF oder anderen Frameworks aufbauen.

Diskutierte Konzepte:

- Farben;
- Stroke;
- Füllungen;
- Linienbreite und Linienart;
- Textstile;
- Symbolstile;
- Themes.

### 5.5 Rendering und Export

Als erster Renderer wird **SVG** bevorzugt, weil es:

- textbasiert ist;
- leicht geprüft und getestet werden kann;
- gut in Markdown und Repository-Dokumentation funktioniert;
- unabhängig von nativen UI-Frameworks ist;
- deterministische Demo-Ausgaben ermöglicht.

Als spätere Kandidaten wurden genannt:

- Bitmap-Export (PNG/BMP/JPEG je nach Backend);
- Win32/GDI+;
- Direct2D;
- Skia;
- Cairo;
- HTML Canvas;
- experimentelle Terminal-/Sixel- oder textnahe Ausgabe.

Es wurde **nicht** festgelegt, dass alle diese Backends umgesetzt werden müssen. Sie sind Erweiterungskandidaten hinter einer Renderer-Grenze.

### 5.6 Boards und Grids

GameWorks liefert einen guten konkreten Treiber für generische Board-Visualisierung.

Genannte Beispiele:

- Go-Moku-Brett, insbesondere 19 × 19;
- Schachbrett, 8 × 8;
- generisches rechteckiges Zellenraster;
- Karten-Layoutbereiche für spätere Bridge-/Kartenspiel-Demos;
- Koordinatenbeschriftungen;
- Marker und Spielsteine;
- Auswahl-/Highlight-Zustände;
- Markierung des letzten Zuges;
- Hit-Testing.

Das Board-Rendering bleibt rein grafisch. Das Toolkit soll nicht wissen, ob ein Zug legal oder strategisch gut ist.

### 5.7 Charts und mathematische Visualisierung

Das Graphics Toolkit soll auch Numerics-/Math-Projekte unterstützen.

Als erste Richtung wurden diskutiert:

- Funktionsplots;
- Polyline-Plots;
- Scatterplots;
- Balkendiagramme;
- Achsen;
- Rasterlinien;
- Beschriftungen;
- einfache Legenden.

Mögliche spätere Visualisierungen:

- Histogramme;
- Boxplots;
- Heatmaps;
- Suchbaum-/Graphvisualisierung;
- Bewertungsverläufe von Game-AI;
- Data Visualization;
- parametrische Visualisierung.

Das Graphics Toolkit visualisiert Daten, soll aber keine Statistik- oder Numerikalgorithmen übernehmen.

## 6. Entwicklungsstrategie

Ein wichtiger Punkt der Diskussion war, nicht zuerst drei riesige Produkte zu bauen, bevor ein sichtbares Ergebnis entsteht.

Die gewählte Strategie:

1. Graphics und Numerics als eigenständige Projekte führen;
2. konkrete Konsumenten wie GameWorks die ersten Anforderungen treiben lassen;
3. nur Funktionen verallgemeinern, die klar wiederverwendbar sind;
4. den Core frameworkneutral halten;
5. früh sichtbare Ergebnisse erzeugen, zuerst mit SVG;
6. weitere Backends und Abstraktionen nur ergänzen, wenn reale Beispiele sie rechtfertigen.

Zusammengefasst:

> Anwendungen bauen und dabei saubere wiederverwendbare SASD-Bausteine herauslösen, statt isoliert die perfekte universelle Bibliothek zu entwerfen.

## 7. Bevorzugte frühe Demos

### Go-Moku-Brett

Die stärkste erste Demo:

- 19 × 19 Board/Grid;
- Steine als einfache Kreise;
- A–S- und 1–19-Beschriftung;
- letzter Zug hervorgehoben;
- Umrechnung zwischen Brett- und Device-Koordinaten;
- Hit-Testing;
- SVG-Export.

Die Demo ist klein, deckt aber Geometrie, Raster, Styles, Text, Layer, Hit-Testing und Export ab.

### Funktionsplot

Dient zur Validierung von:

- Weltkoordinaten;
- Achsen und Raster;
- Skalierung;
- Linienserien;
- Clipping;
- Beschriftungen und Annotationen.

### Vector Graphics Preview

Dient zur Validierung von:

- Kreisen und Polygonen;
- Koordinatentransformationen;
- Shape-Auswahl/IDs;
- Bounds;
- Guides;
- einfachen geometrischen Annotationen.

Diese drei Demos bilden zusammen ein ausgewogenes frühes Testfeld für Spielbretter, mathematische Plots und allgemeine 2D-Grafik.

## 8. Visuelles Anwendungskonzept aus diesem Chat

Das bei der Repository-Einrichtung zunächst erzeugte Preview-Bild wurde später als weniger ansprechend beurteilt als Screenshots anderer SASD-Repositories. Daraufhin wurde in diesem Chat ein neues **fotorealistisches Desktop-Anwendungsbild** erzeugt.

Die bevorzugte Richtung ist eine professionell wirkende Graphics-Workbench statt einer schematischen Architekturillustration.

Das erzeugte Konzept zeigt unter anderem:

- eine dunkle professionelle Desktop-Anwendung;
- Navigation für Project/Assets/Demos links;
- Dokument-Tabs;
- Arbeitsbereich **Go-Moku Board**;
- Arbeitsbereich **Function Plot**;
- **Vector Graphics Preview**;
- Properties-/Layers-/History-Panels;
- Bedienelemente für Coordinate Mapping;
- SVG-Export-Einstellungen;
- eine visuelle Galerie mit Board-, Plot-, Vector-, Surface-, Data-Visualization- und Parametric-Beispielen;
- Statusangaben wie Cursorposition, ausgewählte Geometrie, Backend, Zoom und Exportbereitschaft.

Dieser Screenshot ist eine **aspirative Produktvisualisierung** und kein Nachweis, dass die gezeigten Funktionen bereits implementiert sind.

Der Nutzer hat dieses fotorealistische Anwendungsbild ausdrücklich dem bisherigen schematischen SVG-Preview vorgezogen und darum gebeten, es als Repository-Screenshot zu verwenden. Falls dieser Austausch noch nicht committed wurde, sollte er als Präsentationsaufgabe weitergeführt werden.

## 9. Genannte Referenzprodukte und -projekte

Nicht alle genannten Produkte sind direkte Vorlagen des Graphics Toolkit, aber sie liefern wichtigen Kontext.

### Direkte bzw. starke Grafikreferenzen

**Skia / SkiaSharp**

Referenz für ausgereiftes 2D-Rendering von Pfaden, Formen, Text, Bildern, Filtern und Cross-Platform-Ausgabe. Das Graphics Toolkit soll nicht Skia komplett nachbauen; Skia ist eher potenzielles Backend und Qualitätsreferenz.

**MonoGame**

Nützlich als Referenz für klare Rendering-Loops, Content Handling und zugängliche Game-/Grafikarchitektur. Nicht das Zielmodell des Toolkit-Core.

**raylib**

Interessant wegen bewusst kleiner, verständlicher APIs und lehrfreundlicher Beispiele. Das passt zur gewünschten Richtung kompakter Demos und geringer konzeptioneller Hürde.

### Benachbarte Game-/AI-Referenzen

**OpenSpiel** und **Ludii** wurden vor allem für GameWorks-Architektur und Spielmodellierung diskutiert. Für Graphics Toolkit sind sie indirekt wichtig, weil sie die Trennung zwischen Spielzustand/Spielalgorithmen und Visualisierung unterstreichen.

**Stockfish**, **Leela Chess Zero**, **DDS**, **WBridge5** und **Bridge Base Online** sind Domänenreferenzen für GameWorks, keine direkten Ziele des Graphics Toolkit.

### Benachbarte Numerikreferenzen

**Math.NET Numerics**, **ALGLIB**, **NAG**, **IMSL** und **GSL** wurden als Referenzen für die Numerikseite des SASD-Ökosystems genannt. Für Graphics Toolkit ist vor allem die Integrationsgrenze wichtig: numerische Ergebnisse visualisieren, aber numerische Algorithmen nicht in die Rendering-Bibliothek hineinziehen.

## 10. Repository-Baseline aus der Diskussion

Im Verlauf dieses Chats wurde aus dem minimalen Repository ein strukturiertes Projektfundament aufgebaut. Festgelegt bzw. eingerichtet wurden:

- öffentliches Repository `Robin-Goerlach/SASD-Graphics-Toolkit`;
- C++20/CMake-Basis;
- Struktur mit `include/`, `src/`, `tests/`, `docs/` und `assets/`;
- GitHub-Actions-CMake-Workflow als Build-Baseline für Windows und Linux;
- README mit Screenshot/Preview und Projektgrenzen;
- Architektur-, Feature-, Roadmap- und Integrationsdokumentation;
- `AGENTS.md` für KI-gestützte Entwicklung;
- Contribution- und Changelog-Dokumente;
- die vorhandene **MIT License** wurde beibehalten und explizit dokumentiert.

Die MIT-Lizenz war bereits im Repository vorhanden. Dies wurde im Chat überprüft, nachdem zwischenzeitlich fälschlich angenommen worden war, die Lizenzentscheidung sei noch offen.

## 11. Dokumentations- und Sprachregel

Später wurde ausdrücklich entschieden:

- **Englisch ist die Standardsprache**.
- Deutsche Dokumente sind Begleitfassungen.
- Deutsche Begleitdateien verwenden nach Möglichkeit `.de.md`.
- Öffentlich sichtbare Standardlinks zeigen zuerst auf Englisch.
- Die englische `LICENSE` ist rechtlich maßgeblich.
- `LICENSE.de.md` ist nur eine nicht rechtsverbindliche deutsche Lesehilfe.

Die Struktur soll weitere Sprachen später ermöglichen, ohne das Repository erneut grundlegend umzubauen.

## 12. Lizenzentscheidung

Das Repository verwendet die **MIT License**.

Für die aktuelle Baseline ist das keine offene Designfrage mehr. Dokumente sollten die Lizenz nicht als unentschieden darstellen, solange keine spätere bewusste Änderung beschlossen wird.

## 13. Produktphilosophie aus der Diskussion

Das Graphics Toolkit soll:

- klein beginnen, bevor es breit wird;
- verständlich und gut dokumentiert sein;
- außerhalb von GameWorks wiederverwendbar sein;
- ohne GUI testbar sein;
- im Core backendunabhängig bleiben;
- durch nützliche Beispiele getrieben werden;
- für Lehre und Forschung ebenso wie für Anwendungen geeignet sein;
- klar zwischen implementierten Funktionen und Roadmap-Ideen unterscheiden.

Als Leitmotiv wurde festgehalten:

> Zeichne nicht nur Pixel. Zeichne Modelle, die man verstehen, testen und wiederverwenden kann.

## 14. Punkte, die bis zu einer separaten Entscheidung nicht normativ sind

Folgende Ideen wurden diskutiert, sollen aber nicht automatisch als Verpflichtung gelten:

- genaue Reihenfolge der Renderer-Backends nach SVG;
- Unterstützung aller Bitmap-Formate;
- Terminal/Sixel-Ausgabe;
- HTML-Canvas-Export;
- 3D-Oberflächen;
- fortgeschrittene parametrische Visualisierung;
- genaue Integration mit SASD UI Toolkit / UI Platform;
- Sprachbindungen für C# oder andere Sprachen;
- Packaging-/Package-Manager-Strategie;
- endgültige öffentliche API-Namenskonventionen über die aktuelle C++-Richtung hinaus.

Diese Punkte sind sinnvolle Kandidaten, benötigen aber eigene Entscheidungen, Implementierung oder ADRs.

## 15. Verdichtetes Ergebnis

Die wichtigste Richtung aus diesem Chat lautet:

> **SASD Graphics Toolkit soll ein eigenständiges modernes C++20-Fundament für Grafik und Visualisierung werden. Reale Anforderungen aus GameWorks und Numerics treiben die ersten Schritte, ihre Fachlogik bleibt aber außerhalb. Der Start erfolgt mit Geometrie, Koordinatenabbildung, Scene-/Style-Modell, SVG und konkreten Demos. Weitere Abstraktionen und Backends kommen erst hinzu, wenn reale Konsumenten sie rechtfertigen.**
