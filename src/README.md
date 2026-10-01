# src

Dieses Verzeichnis ist für die spätere C++-Implementierung vorgesehen.

Vorgeschlagene Struktur:

```text
src/
├── core/
├── rendering_svg/
├── boards/
├── charts/
└── demo/
```

Der produktive Core sollte unabhängig von konkreten UI- und Rendering-Frameworks bleiben. Renderer und Demos werden in eigenen Modulen ergänzt.
