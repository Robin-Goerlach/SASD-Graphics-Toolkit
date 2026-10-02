# Sprachunterstützung
Dokument-ID: GFX-DOC-SUPPORT.

## Implementierungsplattformen
| Plattform | Art | Aktueller Nachweis | Grafikfähigkeiten |
|---|---|---|---|
| cpp | gleichrangige Implementierung, zuerst | C++20-/CMake-Gerüst, Repository-CTest-Prüfung | keine implementiert |
| dotnet | geplante gleichrangige Implementierung | reservierte Quell-/Test-/Beispielpfade | keine implementiert |

Noch keine Bibliotheksziele, .NET-Projekte, Pakete, Renderer, ausführbaren Beispiele
oder Cross-Language-Konformitätsrunner vorhanden.
CMake/CTest prüft derzeit ausschließlich Repository-Konsistenz.
Unterstützungsmetadaten stehen in [project.json](../../spec/project.json).

## Natürliche Sprachen
| Locale | Dokumentation | Textkataloge | Laufzeit |
|---|---|---|---|
| en | Standard, vorhanden | leeres UTF-8-JSON-Gerüst | nicht implementiert |
| de | Begleitfassung, vorhanden | leeres UTF-8-JSON-Gerüst | nicht implementiert |

## Unterstützung ergänzen
Plattformpfade nur mit ausdrücklichem Umfang anlegen. Echte Builds, Tests, Beispiele
und gemeinsame Vektor-Runner ergänzen, bevor Fähigkeiten als implementiert gelten.
Weitere Dokumentationssprachen mit Übersetzungen und geprüften Quellhashes registrieren.
Gleiche Textschlüssel beweisen weder Übersetzungsqualität noch Font-/Schriftformungsunterstützung.
