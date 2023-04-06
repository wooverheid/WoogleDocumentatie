# OpenWebConcept als eenduidige en generaliseerbare standaard

- Zorg ervoor dat attributen die hetzelfde betekenen ook dezelfde namen krijgen
    - Voorbeeld: `Titel_Bijlage` (woo-verzoek) en `Naam_Bijlage` (convenant)
    - Onze toevoeging: gebruik bestaande specificatie (Dublin Core) en maak daarbovenop een nieuwe Openpub specificatie voor Woo-specifieke metadatavelden om een heldere, eenduidige specificatie te maken die heel gemakkelijke kan worden hergebruikt en aangevuld voor nieuwe Woo-categorieen
    - Maak een 'basis' met attributen zoals een 'titel', 'publicatiedatum' etc. die voor elke informatiecategorie gelden en hetzelfde zijn
- Maak het mogelijk om URL's naar publicaties af te leiden uit de API
    - Overal dezelfde taal spreken = duidelijkheid en voorspelbaarheid = snelheid en efficientie
    - Ons voorstel: gebruik 'iets' om het type publicatie aan te geven, bijvoorbeeld `woo-verzoeken` en plak daarachter een `slug` in combinatie met een of andere `identifier` (bijvoorbeeld: UUID) om een unieke url te genereren
    - `https://www.gemeentehw.nl/woo-verzoeken/woo-verzoek-over-appm-facturen/e8e71f20-da24-41e8-854f-5bb7105bce8b`
    - `https://www.gemeentehw.nl/woo-verzoeken/` laat dan alle Woo-verzoeken zien
    - Hoe kan de gebruiker van de API hier dan bij? Simpel, we plaatsen een `opub:baseUrl` (zoals https://www.gemeentehw.nl/woo-verzoeken) en een `opub:itemUrlFormat` om het formaat aan te geven (zoals 'baseurl/opub:slug/opub:UUID') op het hoogste niveau van het resultaat van de API!

## Basis

Ons voorstel is om een basis samen te stellen met attributen die in elk item voor kunnen komen, ongeacht de informatiecategorie. Zie onderstaand voorbeeld uit `convenant_new.json`:

```
"dc:title": "Afvalwaterakkoord",
"opub:status": "Nieuw",
"dc:description": "In dit bestuursakkoord is afgesproken door de koepelorganisaties, dat het waterschap en de gemeenten moeten
                    samenwerken in de afvalwaterketen als ware het een bedrijf.",
"dc:dateModified": "2023-01-04T16:57:14",
"dc:identifier": "632927",
"dc:UUID": "34de7939-145a-4468-b529-087ad5741ee2",
"dc:datePublication": "2022-11-14",
"opub:theme": "Mileu",
"opub:subTheme": "Waterschap Hollandse Delta",
"opub:slug": "afvalwaterakkoord",
"dc:publisher": "gm0489",
"dc:type": "2f"
```

Al deze velden komen ook voor in de rest van de voorbeelden. Een gebruiker weet dus dat hij, welk dossier hij dan ook voor zich heeft, met `dc:title` de titel van de publicatie kan pakken.

Dit is een voorbeeld, zie ook [het metadata schema](../SPEC%20MetadataSchema/README.md) voor nogmaals onze specificatie (Woogle) waarin we ook een voorzet doen tot het maken van een basis.

## Voorbeelden

Voorbeelden zijn `woo_verzoek_new_json`, `convenant_new.json`, `news_new.json`. Vergelijk deze maar eens met de `_current.json` bestanden.

- Standaardisatie met namespaces: attributen van Dublin Core en eigen namespace `opub`
- Alles naar Engels om eenduidigheid te houden met Dublin Core
- Toevoeging TOOI code van gemeente als `dc:publisher` (voor als je meerdere gemeenten wilt vergelijken oid)
- Toevoeging type van publicatie (als wetcode)
- Standaardisatie van attributen van bijlagen, eventueel deze attributen ook voor verzoek, besluit etc.
- Op het hoogste niveau zijn de 'base url' en het 'url formaat' toegevoegd om API gebruikers in staat te stellen om zelf de url met content te construeren.

### Beschikking

Een nieuwe informatiecategorie toevoegen is erg gemakkelijk: gewoon de basis gebruiken en wat specifieke velden toevoegen die gaan over de informatiecategorie. Op basis van jullie API en ons voorstel hebben we gemakkelijk een voorbeeld kunnen maken van het toevoegen van Beschikkingen (informatiecategorie 2k van de Woo). Zie hiervoor het bestand `beschikking_new.json`. Dit is een van de beschikkingen die wij reeds in Woogle hebben geïndexeerd.

## Opbrengsten

- Eenduidige metadata zorgt ervoor dat gebruikers van de API niet iedere keer weer moeten uitzoeken wat voor namen er zijn bedacht voor attributen. Het is heerlijk om te weten dat je altijd de titel kunt vinden met een bepaalde attribuutnaam. Hetzelfde geldt voor bijlagen, waarbij het belangrijk is om die snel te kunnen vinden en waarbij de structuur dus altijd hetzelfde moet zijn.
- Het gebruik van Dublin Core maakt attributen vinden erg gemakkelijk; deze kun je gewoon Googlen en zijn algemeen bekend!
- Een metadata basis en specificatie zorgen ervoor dat niet iedereen weer opnieuw het wiel hoeft uit te vinden. Met andere woorden: het is al duidelijk welke attributen er sowieso in een publicatie zitten!
- Het resultaat van eenduidige URLs is simpel: het stelt gebruikers in staat om heel gemakkelijk door te kunnen linken naar jullie publicaties! Ook 'scrapers' zoals wij zijn er erg blij mee; we kunnen naast de informatie uit de API ook informatie halen van de website zelf!