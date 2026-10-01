# Integration mit GameWorks Lab und Numerics

Dieses Dokument erklärt, wie das **SASD Graphics Toolkit** mit verwandten SASD-Projekten zusammenspielen soll.

## Rolle des Graphics Toolkit

Das Graphics Toolkit ist für Visualisierungs-Infrastruktur zuständig:

- Zeichenmodelle,
- Geometrieprimitive,
- Koordinaten-Mapping,
- Szenen- und Layer-Strukturen,
- Renderer,
- Brett- und Chart-Visualisierungshilfen.

Es soll keine Fachlogik besitzen.

## GameWorks Lab

**SASD GameWorks Lab** soll Spielregeln, Spielzustände, legale Züge, Bewertung, Suche und KI-Logik besitzen.

Das Graphics Toolkit kann bereitstellen:

- generische Raster,
- Go-Moku-Brettdarstellung,
- Schachbrettdarstellung,
- Koordinatenbeschriftungen,
- Marker für den letzten Zug,
- Hit-Testing von Ausgabeposition auf Brettkoordinate,
- später Suchbaum- oder Bewertungsdiagramme.

Faustregel:

> GameWorks entscheidet, was eine Stellung bedeutet. Graphics entscheidet, wie sie gezeichnet wird.

## Numerics / Math Toolkit

**SASD Numerics / Math Toolkit** soll numerische Algorithmen, Statistik, Funktionen, Interpolation, Optimierung und mathematische Modelle besitzen.

Das Graphics Toolkit kann bereitstellen:

- Achsen,
- Plotbereiche,
- Linien- und Punktserien,
- Skalierung und Koordinaten-Mapping,
- Legenden,
- exportierbare SVG-Diagramme.

Faustregel:

> Numerics berechnet Werte. Graphics stellt Werte dar.

## UI Toolkit / UI Platform

**SASD UI Toolkit** und **SASD UI Platform** können später den Graphics Core für wiederverwendbare Zeichenprimitive, Vorschaukomponenten oder Renderer-Adapter nutzen.

Der Core des Graphics Toolkit sollte nicht von UI-Projekten abhängen. UI-Projekte dürfen vom Graphics Toolkit abhängen, nicht umgekehrt.

## Abhängigkeitsrichtung

Bevorzugte Richtung:

```text
GameWorks Lab  ---> Graphics Toolkit
Numerics       ---> Graphics Toolkit
UI Toolkit     ---> Graphics Toolkit
```

Vermeiden:

```text
Graphics Toolkit ---> GameWorks Lab
Graphics Toolkit ---> Numerics
Graphics Toolkit ---> UI Toolkit Core-Logik
```

## Erstes gemeinsames Szenario

Das erste praktische Integrationsszenario sollte ein Go-Moku-Brett sein:

1. GameWorks erzeugt einen Brettzustand.
2. Graphics wandelt den Brettzustand in eine Szene um.
3. Der SVG-Renderer schreibt die Szene in eine SVG-Datei.
4. Tests prüfen Brettkoordinaten und SVG-Struktur.
