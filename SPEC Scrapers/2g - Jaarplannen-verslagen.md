# 2g - Jaarplannen en -verslagen

## Overzicht scrapers
- [Open overheid](https://open.overheid.nl/)

[Hier](../SPEC%20MetadataSchema/README.md) zijn alle metadata velden te vinden die we (indien beschikbaar) opslaan.

## Open overheid

Scraper source op [Github](https://github.com/wooverheid/WooScrapers/blob/main/Spiders/SpiderOpenOverheid.py).

### Dagelijks
Dagelijks halen we alle jaarplannen en -verslagen op via de link: https://open.overheid.nl/zoekresultaten?informatiesoort=c_3d782f30 door middel van een webscraper.

De jaarplannen en -verslagen worden bij ons geupload als ze geen bekende URL hebben. Dit betekent ook dat wijzigingen achteraf in bij ons bekende adviezen **niet** worden doorgevoerd. Ook worden ze niet verwijderd als ze niet meer op de bron website staan.
