# Scrapers 2k - Beschikkingen

## Overzicht scrapers
- [Officiele bekendmakingen](https://zoek.officielebekendmakingen.nl/)

[Hier](../SPEC%20MetadataSchema/README.md) zijn alle metadata velden te vinden die we (indien beschikbaar) opslaan.

## Officiele bekendmakingen

Scraper source op [Github](https://github.com/wooverheid/WooScrapers/tree/main/Beschikkingen).

### Dagelijks
Dagelijks halen we alle beschikkingen op van de afgelopen dag voor **waterschappen, provincies en gemeenten**. Dit doen we door publicaties op te halen via een XML feed van repository.overheid.nl (voorbeeld: https://repository.overheid.nl/sru?&query=(dt.date=2024-09-10) voor alles op 10 september 2024). Deze XML wordt publicatie voor publicatie geparsed naar een valide JSON bestand, die wordt geupload naar onze database. 

Ditzelfde wordt gedaan voor beschikkingen van de **staatscourant**, met beschikkingen van **waterschappen, provincies, gemeenten, ministeries, zelfstandige bestuursorganen, samenwerkingsorganisaties en overige organisaties**. Deze kunnen met behulp van dezelfde SFTP server worden opgehaald.

Deze link wordt gebruikt om de XML feed op te halen:
```
https://repository.overheid.nl/sru?&query=((dt.type=="andere beschikking")or(dt.type=="andere vergunning")or(dt.type=="evenementenvergunning")or(dt.type=="exploitatievergunning")or(dt.type=="omgevingsvergunning")or(dt.type=="vergunning voor activiteiten op of in oppervlaktewater") AND dt.available>="{str(start_date)}" AND dt.available<="{str(end_date)}" AND c.content-area="{publisher_type}")&maximumRecords={batch_size}
```

`publisher_type` kan zijn: `wsb` (waterschappen), `gmb` (gemeenten), `prb` (provincies) of `stcrt` (staatscourant).

De bestanden worden bij ons geupload als ze geen bekende URL hebben. Dit betekent ook dat wijzigingen achteraf in bij ons bekende bestanden **niet** worden doorgevoerd. Ook worden ze niet verwijderd als ze niet meer op de bron website staan.

### Wekelijks/maandelijks
Er worden geen beschikkingen wekelijks of maandelijks opgehaald wegens de enorme omvang van dit corpus. We gaan er vanuit dat de dagelijkse updates voldoende zijn, en dat er geen publicaties in het verleden zijn.

