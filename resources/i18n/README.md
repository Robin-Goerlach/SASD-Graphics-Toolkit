# Message catalog scaffold
[Deutsch](README.de.md).

Catalogs are empty UTF-8 JSON objects mapping stable message keys to strings.
There is no localization runtime yet. Add keys with the first real demo/tool.
Register additional locales in [project.json](../../spec/project.json).
Keep key sets aligned; future runtime policy is selected locale, then English fallback.
Do not translate user data, contract IDs, API identifiers or technical SVG numbers.
See [language development](../../docs/en/050_Multilanguage_Development.md).
