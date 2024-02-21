# Scrapers 2k - Beschikkingen

## Overzicht scrapers
- [Officiele bekendmakingen](https://zoek.officielebekendmakingen.nl/)

[Hier](../SPEC%20MetadataSchema/README.md) zijn alle metadata velden te vinden die we (indien beschikbaar) opslaan.

## Officiele bekendmakingen

### Dagelijks
Dagelijks halen we alle beschikkingen op van de afgelopen dag voor **waterschappen, provincies en gemeenten**. Dit doen we door verbinding te maken met de SFTP server van officiele bekendmakingen: bestanden.officielebekendmakingen.nl. Hiermee halen we XML bestanden op die worden verwerkt tot compacte JSON bestanden. Deze JSON bestanden worden vervolgens geupload naar onze database. 

De bestanden worden bij ons geupload als ze geen bekende URL hebben. Dit betekent ook dat wijzigingen achteraf in bij ons bekende bestanden **niet** worden doorgevoerd. Ook worden ze niet verwijderd als ze niet meer op de bron website staan.

### Wekelijks/maandelijks
TODO
