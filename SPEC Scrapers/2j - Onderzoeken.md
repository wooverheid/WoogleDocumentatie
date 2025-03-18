# 2j - Onderzoeken

## Overzicht scrapers
- [Open overheid](https://open.overheid.nl/)
- [RIVM](https://www.rivm.nl/publicaties)
- [Gemeente Amsterdam](https://onderzoek.amsterdam.nl)

[Hier](../SPEC%20MetadataSchema/README.md) zijn alle metadata velden te vinden die we (indien beschikbaar) opslaan.

## Open overheid

Scraper source op [Github](https://github.com/wooverheid/WooScrapers/blob/main/Spiders/SpiderOpenOverheid.py).

### Dagelijks
Dagelijks halen we alle onderzoeken **van de afgelopen maand** op via de link: https://open.overheid.nl/zoekresultaten?informatiesoort=c_3300f29a&datumrange=afgelopen-maand door middel van een webscraper.

De onderzoeken worden bij ons geupload als ze geen bekende URL hebben. Dit betekent ook dat wijzigingen achteraf in bij ons bekende onderzoeken **niet** worden doorgevoerd. Ook worden ze niet verwijderd als ze niet meer op de bron website staan.

## RIVM

Scraper source op [Github](https://github.com/wooverheid/WooScrapers/blob/main/Spiders/SpiderRIVM.py).

### Dagelijks
Dagelijks halen we alle onderzoeken **van het huidige jaar** op via de link: https://www.rivm.nl/publicaties?f%5B0%5D=bibcite_year%3A{datetime.datetime.now().year}&f%5B1%5D=publications_type%3Areport&page=%2C door middel van een webscraper.

De onderzoeken worden bij ons geupload als ze geen bekende URL hebben. Dit betekent ook dat wijzigingen achteraf in bij ons bekende onderzoeken **niet** worden doorgevoerd. Ook worden ze niet verwijderd als ze niet meer op de bron website staan.

### Wekelijks
Wegens de grote omvang van het complete corpus is er na een volledige historische upload momenteel geen wekelijkse scraper. Ervaring leert dat er geen tot heel weinig onderzoeken in het verleden worden toegevoegd.

## Gemeente Amsterdam

Scraper source op [Github](https://github.com/wooverheid/WooScrapers/blob/main/Spiders/SpiderOnderzoekAmsterdam.py).

### Dagelijks
Dagelijks halen we alle onderzoeken van https://onderzoek.amsterdam.nl op door middel van de gefaciliteerde API. Dat wordt gedaan met de volgende API call: `https://cms.onderzoek-en-statistiek.nl/api/publications?populate=*&pagination[page]=1&pagination[pageSize]=10000`. 

De onderzoeken worden bij ons geupload als ze geen bekende URL hebben. Dit betekent ook dat wijzigingen achteraf in bij ons bekende onderzoeken **niet** worden doorgevoerd. Ook worden ze niet verwijderd als ze niet meer op de bron website staan.

