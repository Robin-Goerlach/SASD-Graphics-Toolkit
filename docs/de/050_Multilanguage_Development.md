# Mehrsprachige Entwicklung
Dokument-ID: GFX-DOC-LANGUAGES.

## Unabhängige Dimensionen
Implementierungsplattformen (`cpp`, `dotnet`, später weitere) und natürliche Sprachen
(`en`, `de`, später BCP-47-Tags) sind unabhängig.
Das Repository folgt dem Math-Toolkit-Aufbau. Die Registrierung in
[project.json](../../spec/project.json) erweitern, benötigte Plattformpfade anlegen
und echte Build-/Testjobs erst ergänzen, wenn Code existiert.

## Gemeinsames Verhalten, idiomatische APIs
Englische Vertragskennungen und maschinenlesbare Daten bleiben über Plattformen stabil.
Natürliche C++-/ .NET-Konventionen für Namen, Besitz und Fehler verwenden.
Diese Mechanismen denselben dokumentierten fachlichen Ergebnissen zuordnen.
Eine gleichrangige Implementierung besitzt eigenen Code; ein Binding delegiert.
Unterschied und unterstützte Fähigkeiten vor Veröffentlichung dokumentieren.

## Dokumentationsablauf
Englisch ist die normative Standardfassung; deutsche Fassungen vermitteln dieselben Entscheidungen.
Entwürfe dürfen auf Deutsch entstehen; vor Abschluss beide Fassungen abgleichen.
Root-Einstiege behalten `.de.md`; Fachtexte liegen in `docs/en/` und `docs/de/`.
Stabile Dokument-IDs verbinden Fassungen in [documentation.json](../../spec/documentation.json).
Lokalisierte Dateinamen dürfen abweichen; Paarungen nicht aus Namensähnlichkeit ableiten.
Alte Dokumentationspfade enthalten Weiterleitungen statt unabhängig gepflegter Texte.

Bei Inhaltsänderungen:
1. Englisches Dokument und deutsche Fassung bearbeiten.
2. Deutschen Inhalt gegen die geänderte englische Quelle prüfen.
3. Im Repository-Root `python3 tools/check_repository.py --print-source-hashes` ausführen.
4. Den geprüften englischen SHA-256-Wert beim zugehörigen Übersetzungseintrag hinterlegen.
5. `python3 tools/check_repository.py` ausführen.

Der Quellhash erkennt einen veralteten Quellenstand; er bewertet keine Übersetzungsqualität.
Pfade und Links werden geprüft, nicht die Verfügbarkeit externer Websites.
Fehlende Übersetzungen kenntlich machen; Fallback-Texte nicht als Übersetzung ausgeben.
Für eine neue Sprache Dokument-/Ressourcenzuordnungen und geprüfte Hashes ergänzen.

## Kommentare und Begriffe
API-Bezeichner und primäre Codekommentare sind Englisch.
Erklärende C++-`//` oder `/** */` und C#-`///`-Kommentare verwenden, wenn Absicht,
Invarianten und Besitz erläutert werden müssen.
Deutsche Entwicklererklärungen gehören in die deutschen Dokumente.
Das deutsch/englische Glossar in den [Verträgen](060_Contracts.md) synchron halten.

## Anwendungslokalisierung — vorbereitet, nicht implementiert
[resources/i18n](../../resources/i18n/README.de.md) enthält UTF-8-JSON-Textkataloge.
Die Kataloge sind leer; Sprachwechsel und Laufzeit-Fallback existieren noch nicht.
Spätere Demos verwenden stabile Textschlüssel, wählen Sprache explizit und fallen auf Englisch zurück.
Das Verhalten des Graphics-Cores darf nicht von globalen Prozesseinstellungen abhängen.
Benutzertitel/Legenden bleiben erhalten und werden nicht automatisch übersetzt.
Technische SVG-Zahlen verwenden Dezimalpunkte; sichtbare Beschriftungen dürfen lokalisiert werden.
Unicode/XML-Escaping ist erforderlich; komplexe Schriftformung, Fonts und bidirektionales
Layout benötigen ausdrücklich ausgewiesene Backend-Fähigkeiten statt pauschaler Sprachversprechen.
