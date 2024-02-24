# 1e-i - Woo-index

## Overzicht scrapers
- [Organisaties overheid](https://organisaties.overheid.nl/woo)

[Hier](../SPEC%20MetadataSchema/README.md) zijn alle metadata velden te vinden die we (indien beschikbaar) opslaan.

## Organisaties overheid

Scraper source op [Github](https://github.com/wooverheid/WooScrapers/blob/main/Spiders/SpiderIndex.py)

### Dagelijks
Op basis van de laatste export (https://organisaties.overheid.nl/archive/exportOO.xml) halen we alle Woo-index gegevens op van organisaties.overheid.nl. Dit is een XML bestand met informatie uit bijvoorbeeld https://organisaties.overheid.nl/woo/38122/Gemeente_Utrecht. Dagelijks halen we de complete index op en beslissen voor elke organisatie:
- Als de organisatie (de index) nog niet bekend is bij ons, dan wordt deze toegevoegd.
- Als de organisatie (de index) al bekend is bij ons, maar de gegevens afwijken (URL, titel of beschrijving voor een van de links is gewijzigd, of er zijn meer links toegevoegd), dan wordt deze bijgewerkt -> we verwijderen de oude en uploaden de nieuwe
- Als de organisatie (de index) al bekend is bij ons, en de gegevens zijn gelijk, dan wordt enkel de `foi_updateDate` bijgewerkt.

De resultaten zijn de zien op https://index.wooverheid.nl.
