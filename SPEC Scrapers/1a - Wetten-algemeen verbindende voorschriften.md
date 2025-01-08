# 1a - Wetten en algemeen verbindende voorschriften

## Overzicht scrapers
- [wetten.overheid.nl](https://wetten.overheid.nl/)

[Hier](../SPEC%20MetadataSchema/README.md) zijn alle metadata velden te vinden die we (indien beschikbaar) opslaan.

## wetten.overheid.nl

Scraper source op [Github](https://github.com/wooverheid/WooScrapers/blob/main/Spiders/SpiderWetten.py).

### Wekelijks

Wekelijks worden nieuwe en aangepaste wetten opgehaald van [wetten.overheid.nl](https://wetten.overheid.nl/) met de url: `https://wetten.overheid.nl/uitgebreid_zoeken/zoekresultaat/titelf/0/tekstf/1/d/{current_date}/dx/0/zd/{current_date}/ds/0/dt/1/db/2/sd/{from_date}`. Hierbij is `current_date` de huidige datum (geeft aan dat de wet nu geldig moet zijn) en `from_date` de datum van een week geleden. Alle wetten die in de afgelopen week inwerking zijn getreden worden zo opgehaald. In het geval van een wijziging wordt de wet bekend bij Woogle vervangen door de nieuwe versie.

Tevens worden wetten en regelingen die niet meer geldig zijn (of niet meer effectief) verwijderd uit Woogle. Hiervoor worden alle links opgehaald van wetten die op dit moment geldig zijn en worden deze vergeleken met de links van de wetten die in Woogle staan. Als een link niet meer voorkomt in de lijst van geldige wetten, wordt de wet verwijderd uit Woogle.
