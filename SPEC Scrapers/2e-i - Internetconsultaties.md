# 2e-i - Internetconsultaties

## Overzicht scrapers
- [Internetconsulatie.nl](https://www.internetconsultatie.nl/)

[Hier](../SPEC%20MetadataSchema/README.md) zijn alle metadata velden te vinden die we (indien beschikbaar) opslaan.

## Internetconsultatie.nl

Scraper source op [Github](https://github.com/wooverheid/WooScrapers/blob/main/Spiders/SpiderInternetConsultaties.py).

### Dagelijks
Dagelijks halen we alle internetconsultaties op via de link: https://www.internetconsultatie.nl/geslotenconsultaties/ door middel van een webscraper. Open consultaties worden **niet** opgehaald, omdat deze nog niet compleet zijn (reacties, bevindingen). Naast geplaatste documenten worden ook alle reacties opgehaald, losse tekstvelden worden omgezet naar een simpel `.txt` bestand.

De internetconsultaties worden bij ons geupload als ze geen bekende URL hebben. Dit betekent ook dat wijzigingen achteraf in bij ons bekende internetconsultaties **niet** worden doorgevoerd. Ook worden ze niet verwijderd als ze niet meer op de bron website staan.
