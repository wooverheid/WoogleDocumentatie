# 1e - Bereikbaarheidsgegevens

## Overzicht scrapers
- [Organisaties overheid](https://organisaties.overheid.nl/woo)

[Hier](../SPEC%20MetadataSchema/README.md) zijn alle metadata velden te vinden die we (indien beschikbaar) opslaan.

## Organisaties overheid

Scraper source op [Github](https://github.com/wooverheid/WooScrapers/tree/main/Bereikbaarheidsgegevens).

### Wekelijks

Op basis van de laatste export (https://organisaties.overheid.nl/archive/exportOO.xml) halen we alle bereikbaarheidsgegevens op van organisaties.overheid.nl. Dit is een XML bestand met informatie uit bijvoorbeeld https://organisaties.overheid.nl/woo/38122/Gemeente_Utrecht, maar ook gegevens van medewerkers van deze organisatie. We halen op:
- De organisatiegegevens, waarbij we voor elke organisatie beslissen:
    - Als de organisatie nog niet bekend is bij ons, dan wordt deze toegevoegd.
    - Als de organisatie al bekend is bij ons, updaten we de gegevens. 
- De medewerkersgegevens, waarbij we voor elke medewerker beslissen:
    - Als de medewerker nog niet bekend is bij ons, dan wordt deze toegevoegd.
    - Als de medewerker al bekend is bij ons, updaten we de gegevens.
