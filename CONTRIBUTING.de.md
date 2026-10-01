# Mitwirken

Danke für dein Interesse am **SASD Graphics Toolkit**.

Englisch ist die Standardsprache der Dokumentation. Die englische Standarddatei ist [CONTRIBUTING.md](CONTRIBUTING.md).

## Aktueller Status

Das Projekt befindet sich in der Repository-Baseline- und Konzeptphase. Beiträge sollten sich deshalb auf Klarheit, Struktur, kleine Core-Bausteine und Tests konzentrieren.

## Bevorzugter Beitragsstil

- Änderungen klein und nachvollziehbar halten.
- Dokumentation zusammen mit Code-Änderungen aktualisieren.
- Keine großen Abstraktionen ohne konkrete Demo oder Testfall ergänzen.
- Den Core unabhängig von UI-Frameworks halten.
- Deterministische Tests bevorzugen.

## Scope-Regeln

Passende Beiträge:

- Core-Geometrietypen,
- Koordinaten-Mapping,
- Primitive für das Scene Model,
- SVG-Export,
- Board-/Grid-Helfer,
- einfache Chart-Grundlagen,
- Tests und Dokumentation.

Nicht im Scope:

- Spielregeln,
- Spiel-KI,
- numerische Algorithmen,
- große UI-Frameworks,
- fremde Anwendungslogik.

## Build

```bash
cmake -S . -B build
cmake --build build
ctest --test-dir build
```

## Dokumentationssprache

Öffentliche Standarddateien sollen Englisch sein. Deutsche Begleitdateien verwenden die Endung `.de.md` und sollen fachlich nahe an der englischen Version bleiben.
