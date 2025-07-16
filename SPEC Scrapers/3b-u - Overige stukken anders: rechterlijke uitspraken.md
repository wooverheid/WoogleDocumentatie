# 3b-u Overige stukken anders: rechterlijke uitspraken

## Overzicht scrapers
- [Rechtspraak.nl](https://www.rechtspraak.nl/)

[Hier](../SPEC%20MetadataSchema/README.md) zijn alle metadata velden te vinden die we (indien beschikbaar) opslaan.

## Rechtspraak.nl

Scraper source op [Github](https://github.com/wooverheid/WooScrapers/blob/main/Spiders/SpiderRechtspraak.py).

### Dagelijks

Dagelijks worden de aangepaste (modified) rechterlijke uitspraken opgehaald van [Rechtspraak.nl](https://www.rechtspraak.nl/) met de url: `https://www.data.rechtspraak.nl/uitspraken/zoeken?return=DOC&modified={from_date}&modified={current_date}`. Hierbij is `current_date` de huidige datum en `from_date` de datum van gisteren. Alle rechterlijke uitspraken die in de afgelopen dag zijn aangepast of toegevoegd worden zo opgehaald. In het geval van een wijziging wordt de uitspraak bekend bij Woogle vervangen door de nieuwe versie op basis van de ECLI (European Case Law Identifier).

De uitspraken worden bij ons geupload als ze geen bekende ECLI hebben.