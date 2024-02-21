# 1b-n - Niewsberichten

## Overzicht scrapers
- [OpenPub](https://openwebconcept.nl/bouwblokken)
- [OpenGemeenten](https://www.opengemeenten.nl/)
- [NVWA](https://www.nvwa.nl/)

[Hier](../SPEC%20MetadataSchema/README.md) zijn alle metadata velden te vinden die we (indien beschikbaar) opslaan.

## OpenPub

### Dagelijks
Dagelijks halen we alle nieuwsberichten op door middel van de API van openpub voor de volgende gemeenten:
- [Lansingerland](https://openpub.lansingerland.nl/wp-json/owc/openpub/v1/items)
- [Alkmaar](https://openpub.alkmaar.nl/wp-json/owc/openpub/v1/items)
- [Pijnacker-Nootdorp](https://openpub.pijnacker-nootdorp.nl/wp-json/owc/openpub/v1/items)
- [Hoeksche Waard](https://openpub.gemeentehw.nl/wp-json/owc/openpub/v1/items)
- [Gouda](https://openpub.gouda.nl/wp-json/owc/openpub/v1/items)
- [Dronten](https://openpub.dronten.nl/wp-json/owc/openpub/v1/items)
- [Texel](https://openpub.texel.nl/wp-json/owc/openpub/v1/items)
- [Berkelland](https://openpub.gemeenteberkelland.nl/wp-json/owc/openpub/v1/items)
- [Rijssen-Holten](https://openpub.rijssen-holten.nl/wp-json/owc/openpub/v1/items)
- [De Fryske Marren](https://openpub.defryskemarren.nl/wp-json/owc/openpub/v1/items)
- [Albrandswaard](https://openpub.albrandswaard.nl/wp-json/owc/openpub/v1/items)
- [Barendrecht](https://openpub.barendrecht.nl/wp-json/owc/openpub/v1/items)
- [Ridderkerk](https://openpub.ridderkerk.nl/wp-json/owc/openpub/v1/items)
- [Ommen](https://openpub.ommen.nl/wp-json/owc/openpub/v1/items)
- [Rozendaal](https://openpub.rozendaal.nl/wp-json/owc/openpub/v1/items)
- [Waddinxveen](https://openpub.waddinxveen.nl/wp-json/owc/openpub/v1/items)
- [Noordwijk](https://openpub.noordwijk.nl/wp-json/owc/openpub/v1/items)
- [Buren](https://openpub.buren.nl/wp-json/owc/openpub/v1/items)

De nieuwsberichten worden bij ons geupload als ze geen bekende URL hebben. Dit betekent ook dat wijzigingen achteraf in bij ons bekende nieuwsberichten **niet** worden doorgevoerd. Ook worden ze niet verwijderd als ze niet meer op de bron website staan. 

## OpenGemeenten
Dagelijks halen we alle nieuwsberichten op door middel van een RSS feed van opengemeenten voor de volgende gemeenten:
- [Westland](https://www.gemeentewestland.nl/nieuws.rss)
- [Bergen (NH)](https://www.bergen-nh.nl/nieuws.rss)
- [Ede](https://www.ede.nl/nieuws.rss)
- [Castricum](https://www.castricum.nl/nieuws.rss)
- [Uitgeest](https://www.uitgeest.nl/nieuws.rss)
- [Heiloo](https://www.heiloo.nl/nieuws.rss)
- [Katwijk](https://www.katwijk.nl/nieuws.rss)
- [Bunnik](https://www.bunnik.nl/nieuws.rss)
- [Woudenberg](https://www.woudenberg.nl/nieuws.rss)
- [Wijk bij Duurstede](https://www.wijkbijduurstede.nl/nieuws.rss)
- [Zeist](https://www.zeist.nl/nieuws.rss)
- [De Bilt](https://www.debilt.nl/nieuws.rss)
- [Voerendaal](https://www.voerendaal.nl/nieuws.rss)
- [Dijkenwaard](https://www.dijkenwaard.nl/nieuws.rss)
- [Heemskerk](https://www.heemskerk.nl/nieuws.rss)
- [Heemstede](https://www.heemstede.nl/nieuws.rss)
- [Bloemendaal](https://www.bloemendaal.nl/nieuws.rss)
- [Harderwijk](https://www.harderwijk.nl/nieuws.rss)
- [Ermelo](https://www.ermelo.nl/nieuws.rss)
- [Zeewolde](https://www.zeewolde.nl/nieuws.rss)
- [Tholen](https://www.tholen.nl/nieuws.rss)
- [Schouwen-Duiveland](https://www.schouwen-duiveland.nl/nieuws.rss)
- [Medemblik](https://www.medemblik.nl/nieuws.rss)
- [Veenendaal](https://www.veenendaal.nl/nieuws.rss)
- [Barneveld](https://www.barneveld.nl/nieuws.rss)
- [Rhenen](https://www.rhenen.nl/nieuws.rss)
- [Houten](https://www.houten.nl/nieuws.rss)
- [Soest](https://www.soest.nl/nieuws.rss)
- [Nieuwegein](https://www.nieuwegein.nl/nieuws.rss)

De nieuwsberichten worden bij ons geupload als ze geen bekende URL hebben. Dit betekent ook dat wijzigingen achteraf in bij ons bekende nieuwsberichten **niet** worden doorgevoerd. Ook worden ze niet verwijderd als ze niet meer op de bron website staan.

## NVWA

### Dagelijks
Dagelijks halen we alle nieuwsberichten op van de NVWA via de link: https://www.nvwa.nl/nieuws-en-media/nieuws door middel van een webscraper.

De nieuwsberichten worden bij ons geupload als ze geen bekende URL hebben. Dit betekent ook dat wijzigingen achteraf in bij ons bekende nieuwsberichten **niet** worden doorgevoerd. Ook worden ze niet verwijderd als ze niet meer op de bron website staan.