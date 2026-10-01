# tests

Dieses Verzeichnis ist für spätere Tests vorgesehen.

Vorgeschlagene Struktur:

```text
tests/
├── core/
├── rendering_svg/
├── boards/
└── charts/
```

Besonders wichtig sind Tests für:

- Geometrietypen,
- Bounds-Berechnungen,
- Koordinatentransformationen,
- Board-Hit-Testing,
- SVG-Ausgabe.

Sobald eine CMake-Struktur vorhanden ist, sollen Tests über `ctest --test-dir build` ausführbar sein.
