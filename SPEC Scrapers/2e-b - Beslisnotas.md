# 2e-b - Beslisnotas

## Overzicht scrapers

- [Open overheid](https://open.overheid.nl/)

[Hier](../SPEC%20MetadataSchema/README.md) zijn alle metadata velden te vinden die we (indien beschikbaar) opslaan.

## Open overheid

Scraper source op [Github](https://github.com/wooverheid/WooScrapers/blob/main/Spiders/SpiderOpenOverheid.py).

### Dagelijks
Dagelijks halen we alle beslisnotas voor alle **ministeries** van de **afgelopen maand** op via de link: https://open.overheid.nl/zoekresultaten?informatiesoort=c_2977c34f&filter-id--organisatie=mini&organisatie=mnre1010&organisatie=mnre1034&organisatie=mnre1013&organisatie=mnre1018&organisatie=mnre1040&organisatie=mnre1045&organisatie=mnre1090&organisatie=mnre1130&organisatie=mnre1058&organisatie=mnre1150&organisatie=mnre1153&organisatie=mnre1109&organisatie=mnre1073&organisatie=mnre1025&datumrange=afgelopen-maand door middel van een webscraper. 

De beslisnotas worden bij ons geupload als ze geen bekende URL hebben. Dit betekent ook dat wijzigingen achteraf in bij ons bekende beslisnotas **niet** worden doorgevoerd. Ook worden ze niet verwijderd als ze niet meer op de bron website staan.

### Wekelijks/maandelijks
Wekelijks halen we alle beslisnotas voor alle **ministeries** op via de link: https://open.overheid.nl/zoekresultaten?informatiesoort=c_2977c34f&filter-id--organisatie=mini&organisatie=mnre1010&organisatie=mnre1034&organisatie=mnre1013&organisatie=mnre1018&organisatie=mnre1040&organisatie=mnre1045&organisatie=mnre1090&organisatie=mnre1130&organisatie=mnre1058&organisatie=mnre1150&organisatie=mnre1153&organisatie=mnre1109&organisatie=mnre1073&organisatie=mnre1025&count=1000 door middel van een webscraper.

Op deze manier hopen we eventuele later gepubliceerde beslisnotas alsnog op te halen.

De beslisnotas worden bij ons geupload als ze geen bekende URL hebben. Dit betekent ook dat wijzigingen achteraf in bij ons bekende beslisnotas **niet** worden doorgevoerd. Ook worden ze niet verwijderd als ze niet meer op de bron website staan.