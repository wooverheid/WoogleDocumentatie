# 2j - Onderzoeken

## Overzicht scrapers
- [Open overheid](https://open.overheid.nl/)

[Hier](../SPEC%20MetadataSchema/README.md) zijn alle metadata velden te vinden die we (indien beschikbaar) opslaan.

## Open overheid

Scraper source op [Github](https://github.com/wooverheid/WooScrapers/blob/main/Spiders/SpiderOpenOverheid.py).

### Dagelijks
Dagelijks halen we alle onderzoeken **van de afgelopen maand** op via de link: https://open.overheid.nl/zoekresultaten?informatiesoort=c_3300f29a&datumrange=afgelopen-maand door middel van een webscraper.

De onderzoeken worden bij ons geupload als ze geen bekende URL hebben. Dit betekent ook dat wijzigingen achteraf in bij ons bekende adviezen **niet** worden doorgevoerd. Ook worden ze niet verwijderd als ze niet meer op de bron website staan.

