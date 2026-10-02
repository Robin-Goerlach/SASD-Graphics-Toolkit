# Integration mit Math, GameWorks und UI
Dokument-ID: GFX-DOC-INTEGRATION.

## Zuständigkeiten
Math verantwortet wiederverwendbare mathematische Algorithmen und allgemeine
Geometrie/Transformationen. Graphics verantwortet Szenen, Stile, Renderer,
visuelles Koordinaten-Mapping, Boards und Diagrammdarstellung.
GameWorks verantwortet Spielregeln, Zustände und KI; UI-Projekte Widgets und Interaktion.

## Abhängigkeitsentscheidung
Die bisherige pauschale Regel gegen jede Graphics-zu-Math-Abhängigkeit wird durch
den vorgeschlagenen ADR-GFX-003 in der [Architektur](020_Architecture.md) ersetzt.
Bevorzugte künftige Richtung: Graphics darf ein kleines Math-Geometriemodul verwenden.
Der Math-Core darf nicht von Graphics, UI oder einem Renderer abhängen.
Eine numerische Visualisierungsanwendung bzw. ein Beispiel verbindet Math und Graphics.
Nicht die ganze Math-Bibliothek für ihre Beispieldiagramme von Graphics abhängig machen.

Derzeit ist keine Math-Paket-/Link-/Laufzeitabhängigkeit konfiguriert.
Die bestehende Math-Implementierung ist C#/.NET; dieses Repository startet mit C++.
Gleiche Ordnerstrukturen machen .NET-Typen nicht unmittelbar für C++ nutzbar.
Ein kompatibler Math-C++-Teilumfang oder eine ausdrücklich entschiedene
Interoperabilitätsgrenze muss vor direkter nativer Integration vorhanden sein.
Bei Auswahl der Abhängigkeit tatsächliche Paket-/Lizenz-/API-Anforderungen prüfen.

## Verbraucher
GameWorks und UI dürfen Graphics verwenden; Graphics verwendet deren Cores nicht.
Adapter übersetzen Fachdaten außerhalb des wiederverwendbaren Graphics-Cores in Szenen.
Erstes Szenario bleibt ein kleines Go-Moku-SVG-Board ohne eingebaute Spielregeln.

## Koordinatengrenze
Mathematische Vektoren/Transformationen gehören zu Math; Welt-/Ausgabekonventionen,
Viewport-Größen und sichtbare Stile zu Graphics.
Einheiten, Achsenrichtung und Zuständigkeit für Umwandlungen am Adapter festlegen.
Versteckte Zyklen und doppelte allgemeine Mathematikimplementierungen vermeiden.
