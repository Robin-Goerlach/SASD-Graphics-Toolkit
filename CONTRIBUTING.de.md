# Beiträge
[English](CONTRIBUTING.md).

Änderungen klein, dokumentiert und an echten Verbrauchern ausrichten.
[AGENTS.md](AGENTS.md), [Architektur](docs/de/020_Architecture.md)
und [mehrsprachigen Ablauf](docs/de/050_Multilanguage_Development.md) beachten.
`src/<plattform>/`, `tests/<plattform>/`, `samples/<plattform>/` verwenden.
Gemeinsame Verträge gehören in `spec/`; Laufzeittexte in `resources/i18n/`.
Englisch ist Standard; deutsche Zuordnung und geprüften Quellhash aktualisieren.
Fähigkeiten ehrlich ausweisen; vorbereitete Ordner sind keine Implementierungen.

Der Core umfasst Szenen/Stile/Rendering/visuelle Koordinaten und Boards/Diagramme.
Spielregeln, KI, numerische Algorithmen und UI-Framework-Logik bleiben außerhalb.
Vor allgemeinen mathematischen Grundtypen Math-Zuständigkeit klären.

Ausführen:
```bash
python3 tools/check_repository.py
cmake -S . -B build
cmake --build build --config Release
ctest --test-dir build --output-on-failure -C Release
```
Voraussetzungen: CMake >= 3.22, C++20-fähiger Compiler, Python >= 3.10.
Unter Windows ggf. `python` verwenden. CTest prüft derzeit Repository-Konsistenz;
mit neuem Code aussagekräftige Implementierungstests ergänzen.
