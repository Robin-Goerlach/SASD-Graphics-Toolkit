# Arbeitsregeln
[English](AGENTS.md).

## Architektur
Math-Toolkit-Aufbau verwenden: `src/<plattform>`, `tests/<plattform>`,
`samples/<plattform>`, gemeinsames `spec/` und `docs/<locale>/`.
Durchgehend `cpp` und `dotnet` verwenden, auch für Beispiele; nicht mit `csharp` mischen.
C++20 kommt zuerst; C#/.NET ist gleichrangig geplant, kein zwingender Wrapper.
Weitere Plattformen/Sprachen in [spec/project.json](spec/project.json) registrieren.
Root-AGENTS.md ist maßgeblich; die deutsche Fassung vermittelt dieselben Regeln.

## Umfang und Abhängigkeiten
Core UI-unabhängig halten. Keine Spielregeln, KI oder UI-Framework-Core-Logik.
Vor allgemeinen mathematischen Grundtypen Zuständigkeit und kleine Math-Anbindung
nach [ADR-GFX-003](docs/de/020_Architecture.md) klären.
Math-Core niemals von Graphics abhängig machen. Noch ist keine Math-Abhängigkeit konfiguriert.
Vor öffentlichen APIs die [Verträge](docs/de/060_Contracts.md) lesen.
Laufzeiten/Bindings/große Abstraktionen nur bei tatsächlichem Verbraucherbedarf ergänzen.

## Code und Tests
Plattformtypische APIs, englische Bezeichner und erklärende englische Kommentare:
C++ `//`/`/** */`, C# `///` nach Bedarf.
Absicht, Invarianten und Besitz erläutern statt nur Anweisungen nachzuerzählen.
IO/UI gehören in Beispiele/Adapter. Tests prüfen echtes öffentliches Verhalten.
Künftige Runner verwenden gemeinsame Vektoren mit deren expliziten Toleranzen.
Geometrieinvarianten und SVG-Struktur/Koordinaten gegenüber reinen Pixeltests bevorzugen.

## Dokumentation
Englisch Standard; Deutsch Begleitfassung. Fachtexte in `docs/en/`, `docs/de/`.
Root-Begleitdateien behalten `.de.md`. Dokument-IDs und Übersetzungszuordnungen stehen in
`spec/documentation.json`. Beide Fassungen und geprüfte Quellhashes nach fachlichem
Review aktualisieren; siehe [Ablauf](docs/de/050_Multilanguage_Development.md).
Alte Pfade sind Weiterleitungen, keine zweite redaktionelle Quelle.
Geplant, Gerüst und implementiert unterscheiden; leere Builds sind keine Bibliothekstests.

## Erforderliche Prüfungen
```bash
python3 tools/check_repository.py
cmake -S . -B build -DSASD_GRAPHICS_BUILD_TESTS=ON
cmake --build build --config Release
ctest --test-dir build --output-on-failure -C Release
```
Voraussetzungen: Python >= 3.10, CMake >= 3.22, C++20-fähiger Compiler.
Unter Windows ggf. `python` statt `python3`. Betroffene Plattformen bauen, sobald echter Code existiert.
CTest prüft derzeit nur Repository-Konsistenz; noch keine Numerik-/Renderer-Runner vorhanden.

## Implementierungsreihenfolge
Math-/Geometriegrenze klären, Koordinaten, Szene/Stile, SVG, danach Go-Moku-Beispiel.
Zweite Plattform nach echtem Verbraucherbedarf; keine Dummy-Paketprojekte anlegen.
