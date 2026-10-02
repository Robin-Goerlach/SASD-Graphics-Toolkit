# Gemeinsame Grafikverträge — Entwurf
Dokument-ID: GFX-DOC-CONTRACTS.

Diese Verträge leiten die Implementierung; noch führt keine Grafik-API sie aus.
[spec/contracts.json](../../spec/contracts.json) enthält stabile IDs und Anforderungen.
[Affine Referenzvektoren](../../spec/test-vectors/affine2d.json) sind Eingabe-/Ergebnisdaten,
noch keine implementierte Cross-Language-Testsuite.

## GFX-COORD-001: Affines Mapping
Für Matrixkoeffizienten `[a,b,c,d,tx,ty]` und Punkt `[x,y]`:
`x' = a*x + c*y + tx`; `y' = b*x + d*y + ty`.
Die Formel legt die Serialisierung fest, nicht das Matrix-Speicherlayout einer Sprache.
Für diese Referenzfälle sind endliche Eingaben und erwartete Ergebnisse erforderlich.
Komponentenvergleich:
`abs(actual-expected) <= max(absTol, relTol*abs(expected))`.
Die Fälle verwenden absolute und relative Toleranz 1e-12.
Dies sind fallspezifische Toleranzen, keine universelle Geometriegenauigkeitsgarantie.
Einheiten, Achsenwahl, inverse Abbildung, singuläre Matrizen und ungültige Eingaben
vor Veröffentlichung entsprechender APIs festlegen.

## GFX-SVG-001: Technische Zahlen
SVG-Attribute verwenden sprachunabhängige Dezimalpunkte und endliche Zahlen.
Eine deutsche sichtbare Achsenbeschriftung darf `1,5` zeigen, während die SVG-Koordinate `1.5` bleibt.
Rundung/Präzision und Grenzfalltests müssen vor Implementierung feststehen.

## GFX-TEXT-001: Text
Unicode-Benutzertexte erhalten und passend zum SVG-Text-/Attributkontext XML-escapen.
Texterhalt verspricht weder bestimmte Fonts noch Schriftformung eines Backends.

## GFX-DEP-001: Abhängigkeiten
Der Core ist unabhängig von UI-Frameworks, Spielregeln und Spiel-KI.
Die Math-Core-Abhängigkeitsrichtung steht in ADR-GFX-003; konkrete Integration ist offen.

## Glossar
| Stabiler Begriff | Deutsche Erklärung |
|---|---|
| scene | Szene: Beschreibung der Zeichenobjekte |
| viewport | Viewport: Ausgabebereich |
| bounds | Begrenzung: räumliche Ausdehnung |
| stroke | Kontur: Liniengestaltung |
| fill | Füllung: Flächengestaltung |
| conformance | Konformität: gemeinsames Verhalten erfüllen |

Weitere Verträge betreffen Bounds-Ränder, Normalisierung, Clipping, Z-Reihenfolge,
Fehlersemantik und SVG-Vergleiche. Verträge nach Bedarf der ersten APIs ergänzen.
