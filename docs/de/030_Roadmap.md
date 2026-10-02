# Roadmap
Dokument-ID: GFX-DOC-ROADMAP.

## M0: Mehrsprachige Repository-Grundlage — abgeschlossen
Math-kompatible Plattformbäume; englische/deutsche Dokumentation; Entwicklungsregeln;
Vertragsentwürfe und affine Referenzvektoren; Unterstützungsmatrix; CMake-Delegation;
Repository-/Link-/Übersetzungs-/Ressourcenprüfung in CI.
Noch keine Grafikalgorithmen, Bibliotheksziele oder Cross-Language-Runner implementiert.

## M1: Kleine Mathematik-/Geometriegrenze — geplant
ADR-GFX-003 mit dem Math Toolkit klären. Nur die 2D-Typen und Operationen für die
erste Demo festlegen. Endliche Eingaben, Besitz, Einheiten und Toleranzen beschreiben.
Abnahme: dokumentierte Abhängigkeits-/API-Entscheidung und aussagekräftige Unit-Tests
für die ersten echten C++-Typen. Keine vollständige Math-C++-Portierung erforderlich.

## M2: Koordinaten — geplant
Viewport, Welt-/Ausgabe-Mapping, Skalierung, Translation, Y-Achsenkonvention und Bounds.
Affine Referenzvektoren gegen echte C++-Operationen prüfen, einschließlich inverser
Roundtrips und ungültiger Eingaben.

## M3: Szene und Stile — geplant
Ebenen, Grundformen, Linien-/Füll-/Textstile, stabile IDs und Z-Reihenfolge.

## M4: SVG — geplant
Linien, Rechtecke, Kreise, Polylinien/Text, viewBox, XML-Escaping, Unicode und
sprachunabhängige Zahlenserialisierung. Struktur und Koordinaten testen.

## M5: Boards — geplant
Generisches Grid, Go-Moku-Demo, Schachgrundlage, Marker und Hit-Testing.
Spielregeln bleiben außerhalb des Toolkits.

## M6: Diagramme — geplant
Achsen, Linien-/Scatter-Serien, Legenden und Beispielintegration mit Math.
Lokalisierte sichtbare Beschriftungen von technischen SVG-Zahlen trennen.

## M7: Zweite Implementierung — geplant, nach Verbraucherbedarf
Einen nützlichen C#/.NET-Teilumfang auswählen, keine sofortige Komplettportierung versprechen.
Eigenständig bauen/testen/paketieren; gemeinsame Referenzvektoren in beiden Runnern nutzen.
Fähigkeiten und normale sprachspezifische Fehler-/API-Konventionen dokumentieren.
Weitere Plattformen erst bei konkretem Verbraucherbedarf berücksichtigen.

## M8: Pre-Release — geplant
API-Review, echte Build-/Test-/Paketprüfungen und kleine ausführbare Beispiele.
Unterstützungsstände nur mit ausführbaren Nachweisen aktualisieren.
