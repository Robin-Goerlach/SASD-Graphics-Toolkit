# Architektur
Dokument-ID: GFX-DOC-ARCHITECTURE.

## ADR-GFX-001: Zwei unabhängige Sprachdimensionen — angenommen
Die Math-Toolkit-Konvention wird übernommen: `src/<plattform>/`,
`tests/<plattform>/`, `samples/<plattform>/`, `spec/` und `docs/<locale>/`.
Der vorhandene Plattformschlüssel `dotnet` steht für C#/.NET, `cpp` für C++.
Keine Kombinationen wie `src/cpp/de/` und keine übersetzten Quellcodekopien.
Englisch ist die Standardsprache; Deutsch ist eine Begleitfassung.
Weitere Implementierungsplattformen und Dokumentationssprachen kommen hinzu.

## ADR-GFX-002: Gleichrangige Implementierungen — angenommen
C++20/CMake kommt zuerst. C#/.NET ist als idiomatische gleichrangige Implementierung
geplant und nicht zwingend ein Wrapper um C++.
Gemeinsames Verhalten ist maßgeblich; gemeinsamer Quellcode und identische
API-Schreibweisen sind nicht erforderlich.
Ein Binding delegiert an eine andere Implementierung und muss so ausgewiesen sein.
Optionale Bindings/native Performance-Provider benötigen eine eigene Entscheidung
zu Besitzverhältnissen, Fehlerübertragung, Paketen und Bereitstellung.
Dieser Strukturumbau implementiert weder eine C-ABI noch ein .NET-Projekt.

## Grafikschichten
Anwendungen und Beispiele liefern Fachdaten. Visualisierer bauen Szenen auf.
Szenen enthalten Ebenen, Formen und Darstellungsstile.
Koordinaten-Mapping platziert Objekte; ein Renderer übersetzt sie in die Ausgabe.
SVG ist der erste Renderer. Boards/Grids und kleine Diagramme folgen.
Der Core hängt weder von einem UI-Framework noch von Spielregeln oder Spiel-KI ab.

Geplante C++-Namespaces: `sasd::graphics::{geometry,coordinates,style,scene,boards,charts}`
und `sasd::graphics::rendering::svg`.
Die geplante .NET-Namespace-Wurzel lautet `Sasd.Graphics`.
Dies sind Entwurfsrichtungen, noch keine vorhandenen öffentlichen APIs.

## ADR-GFX-003: Math-Zuständigkeit und Integration — vorgeschlagen
Math verantwortet wiederverwendbare mathematische Algorithmen und Grundtypen;
Graphics verantwortet Szenen, Stile, visuelles Koordinaten-Mapping, Rendering
und Visualisierung. Keine allgemeine Vektor-/Matrix-/Numerikbibliothek in Graphics
unabhängig neu entwickeln.
Bevorzugt werden künftig ein kleines Math-C++-Geometriemodul für C++ Graphics
und der bestehende Math-.NET-Baum für .NET Graphics, bei Bedarf mit Adaptern.
Paketgrenze, Versionen und konkrete API sind noch offen.
Graphics bindet derzeit weder Math ein noch startet es eine .NET-Laufzeit.

Der Math-Core bleibt unabhängig von Graphics. Anwendungen/Beispiele dürfen beide
verbinden. Vor neuen Abhängigkeiten die [Integration](040_Integration_GameWorks_Numerics.md) beachten.

## Prüfung
Gemeinsame Eingaben/Ergebnisse und Toleranzen liegen in `spec/`.
Sprachspezifische Runner führen sie aus, sobald Implementierungen existieren.
Geometrie und SVG-Semantik vergleichen; byte-identische SVG-Dateien oder
pixel-identische Schriftdarstellung über Backends hinweg sind nicht gefordert.
