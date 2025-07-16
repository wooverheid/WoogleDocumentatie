# 2b - Vergaderstukken/verslagen

## Overzicht scrapers
- [Officiele bekendmakingen](https://zoek.officielebekendmakingen.nl/)
- [Tweede Kamer](https://www.tweedekamer.nl/)

[Hier](../SPEC%20MetadataSchema/README.md) zijn alle metadata velden te vinden die we (indien beschikbaar) opslaan.

## Officiele bekendmakingen

Scraper source op [Github](https://github.com/wooverheid/WooScrapers/tree/main/Handelingen).

### Dagelijks
Dagelijks halen we alle vergaderstukken/verslagen op van de afgelopen dag voor de **Tweede Kamer, Eerste Kamer en de Verenigde Vergadering der Staten-Generaal**. Dit doen we door publicaties op te halen via een XML feed van repository.overheid.nl (voorbeeld: https://repository.overheid.nl/sru?&query=(dt.date=2024-09-10) voor alles op 10 september 2024). Deze XML wordt publicatie voor publicatie geparsed naar een valide JSON bestand, die wordt geupload naar onze database. 

Deze link wordt gebruikt om de XML feed op te halen:
```
https://repository.overheid.nl/sru?&query=(dt.available>={str(start_date)} AND dt.available<={str(end_date)} AND dt.type=Handelingen)
```

De bestanden worden bij ons geupload als ze geen bekende URL hebben. Dit betekent ook dat wijzigingen achteraf in bij ons bekende bestanden **niet** worden doorgevoerd. Ook worden ze niet verwijderd als ze niet meer op de bron website staan.

## Tweede Kamer

Scraper source op [Github](https://github.com/wooverheid/WooScrapers/tree/main/Handelingen).

### Dagelijks
Dagelijks halen we alle VOORLOPIGE vergaderstukken/verslagen op van de **Tweede Kamer**. Dit zijn verslagen die nog niet officieel zijn vrijgegeven, maar waar wel een voorlopige versie van beschikbaar is. Dit doen we met behulp van een webscraper op de website [https://www.tweedekamer.nl/kamerstukken/plenaire_verslagen](https://www.tweedekamer.nl/kamerstukken/plenaire_verslagen). De verslagen worden opgehaald voor het huidige vergaderjaar: `https://www.tweedekamer.nl/kamerstukken/plenaire_verslagen/detail/{vergaderjaar}`.

Zodra de versie van Officiele bekendmaking beschikbaar is, vervangen deze het voorlopige verslag op basis van het vergadernummer. 

De bestanden worden bij ons geupload als ze geen bekende URL hebben. Dit betekent ook dat wijzigingen achteraf in bij ons bekende bestanden **niet** worden doorgevoerd. Ook worden ze niet verwijderd als ze niet meer op de bron website staan.