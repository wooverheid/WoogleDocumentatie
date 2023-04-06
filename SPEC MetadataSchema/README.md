# Woogle metadata specificatie
Versie 1.0 - Universiteit van Amsterdam - Maik Larooij, Maarten Marx

We hebben te maken met verschillende informatiecategorieën die vallen onder de Woo. Toch is het belangrijk om deze categorieën op enigzins dezelfde wijze op te slaan, om bijvoorbeeld:
- Tegelijkertijd te kunnen zoeken in alle openbaar gemaakte stukken, bijvoorbeeld resultaten uit convenanten en Woo-verzoeken;
- Te kunnen groeperen op thema, om alle openbaar gemaakte stukken behorend aan een bepaald thema te kunnen doorzoeken;
- Het mogelijk te maken om de groepering anders te laten zijn voor burgers, journalisten of andere nuttigers, bijvoorbeeld het ordenen van een website op thema in plaats van op informatiecategorie. 

De attributen hebben bij ons ook een prefix om aan te geven waar ze vandaan komen:
- [dc -> Dublin Core](https://www.dublincore.org/)
- tooiwl -> TOOI voor themaindeling
- foi -> Freedom of Information, onze eigen namespace voor attributen die niet bestaan in een gangbare standaard

## Woo-basis
De volgende attributen kunnen worden ingezet voor elke informatiecategorie. Deze maken het mogelijk om alle openbaar gemaakte stukken toch met elkaar te kunnen matchen op bijvoorbeeld aanbieder, jaar/publicatiedatum of thema.
| **#** | **Technische naam** | **Naam**            | **Omschrijving**                                                                                                                                                                                              | **Voorbeeld**                                                                                                                                                |
|-------|---------------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1     | dc_identifier       | ID                  | Unieke identifier van een openbaar gemaakt stuk. In de vorm: `land.code.categorie.jaar.nummer`.                                                                                                               | `nl.gm1963.2i.2022.10`                                                                                                                                       |
| 2     | dc_title            | Titel               | Titel van het stuk.                                                                                                                                                                                           | Woo-verzoek over voetbalvereniging Zinkwegse Boys (HSW)                                                                                                      |
| 3     | dc_description      | Beschrijving        | Beschrijving van het stuk.                                                                                                                                                                                    | Verzoeker vraagt om informatie over de aanleg van speelvoorzieningen, extra kleedkamers, vergroting van het parkeerterrein en een gesprek met een omwonende. |
| 4     | dc_publisher        | Aanbieder           | De aanbieder van het stuk, in de vorm van een TOOI code, zie bijvoorbeeld [hier](https://tardis.overheid.nl/waardelijst?work_uri=https%3A%2F%2Fidentifier.overheid.nl%2Ftooi%2Fset%2Frwc_gemeenten_compleet). | `gm1963`                                                                                                                                                     |
| 5     | foi_publishedDate   | Publicatiedatum     | De datum van publicatie van het stuk (YYYY-mm-dd).                                                                                                                                                            | 2022-08-23                                                                                                                                                   |
| 6     | dc_date_year        | Jaar                | Kan worden afgeleid van publicatiedatum of zelf worden ingevuld als minimale eis aan iets van een datum.                                                                                                      | 2022                                                                                                                                                         |
| 7     | tooiwl_topic        | Thema/onderwerp     | Het thema of onderwerp behorend aan het openbaar gemaakte stuk.                                                                                                                                               | ruimte en infrastructuur                                                                                                                                     |
| 8     | dc_type             | Informatiecategorie | De informatiecategorie in de vorm van de wetcode, bijvoorbeeld `2i` voor Woo-verzoeken en `2f` voor convenanten.                                                                                              | `2i`                                                                                                                                                         |
| 9     | dc_source           | Bron (URL)          | De URL waar het stuk kan worden gevonden.                                                                                                                                                                     | https://openpub.gemeentehw.nl/..........                                                                                                                     |
| 10    | dc_creator          | Maker               | Maker van de publicatie in onze database (meestal ook de TOOI code, of bijvoorbeeld een Scraper-versie).                                                                                                      | `gm1963`                                                                                                                                                     |
| 11    | foi_nrDocuments     | Aantal documenten   | Aantal documenten in dit 'dossier'. Wordt niet ingevuld, maar afgeleid van geuploade documenten.                                                                                                              | 6                                                                                                                                                            |
| 12    | foi_linkedDossier   | Gelinkt dossier     | Eerste aanzet tot het mogelijk maken van 'linken' van dossier, bijvoorbeeld deelbesluiten. Waarde is dan de identifier van het gelinkte dossier.                                                              | `nl.gm1963.2i.2022.11`                                                                                                                                       |

### Verplichtingen
Voor onze doeleinden verplichten wij bij het insturen enkel de volgende velden:
- Titel (dc_title)
- Beschrijving (dc_description)
- Informatiecategorie (dc_type)
- Aanbieder (dc_publisher)
- Een vorm van een datum, minimaal het jaar (dc_date_year)
- Een ID (dc_identifier) genereren wij zelf

## Woo-basis voor losse documenten
| **#** | **Technische naam** | **Naam**        | **Omschrijving**                                                                                  | **Voorbeeld**                            |
|-------|---------------------|-----------------|---------------------------------------------------------------------------------------------------|------------------------------------------|
| 1     | dc_identifier       | ID              | Unieke identifier van een document. In de vorm: `land.code.categorie.jaar.nummer.doctype.nummer`. | `nl.gm1963.2i.2022.10.besluit.1`         |
| 2     | dc_title            | Titel           | Titel van het document.                                                                           | Besluitbrief Woo Geredigeerd             |
| 3     | foi_fileName        | Bestandsnaam    | Bestandsnaam van het document. Wordt afgeleid van het opgehaalde document.                        | Besluitbrief-Woo_Geredigeerd.pdf         |
| 4     | dc_source           | Bron (URL)      | URL naar het document.                                                                            | https://openpub.gemeentehw.nl/.......... |
| 5     | dc_type             | Type document   | Type van het document, bijvoorbeeld 'bijlage', 'besluit', 'inventarislijst'.                      | besluit                                  |
| 6     | foi_sentDate        | Datum           | Datum van verzenden of aanmaken document                                                          | 2022-07-21                               |
| 7     | foi_originator      | Verzender       | Verzender van het document.                                                                       | Burgemeester.....                        |
| 8     | foi_recipient       | Ontvanger       | Ontvanger van het document                                                                        | Raadslid.....                            |
| 9     | dc_format           | Bestandsformaat | Formaat van het bestand (MIMEtype). Wordt afgeleid van het opgehaalde document.                   | application/pdf                          |
| 10    | foi_nrPages         | Aantal pagina's | Aantal pagina's van het document. Wordt afgeleid van het opgehaalde document.                     | 8                                        |

Verder zijn er nog een aantal attributen die wij voor onze eigen doeleinden ophalen uit de documenten, zoals de tekst, tekst na OCR, aantal woorden, aantal karakters etcetera.

### Verplichtingen
Voor documenten is niet zoveel verplicht, we willen in ieder geval de URL hebben om hem op te halen (dc_source). Hier halen we zelf al veel uit. Een ID (dc_identifier) genereren we zelf.

## Categorie-specifieke metadata
Deze hebben we nu enkel samengesteld voor de categorie 'Woo/Wob-verzoeken'. De stukken bevatten dus de velden zoals genoemd in de Woo-basis, plus deze velden:

### Woo/Wob-verzoeken (categorie 2i)
| **#** | **Technische naam** | **Naam**     | **Omschrijving**                                                                                 | **Voorbeeld**                                                                                                         |
|-------|---------------------|--------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 13    | foi_requestDate     | Verzoekdatum | Datum van het Wob/Woo-verzoek.                                                                   | 2022-04-12                                                                                                            |
| 14    | foi_decisionDate    | Besluitdatum | Datum van het besluit op het Wob/Woo-verzoek                                                     | 2022-05-01                                                                                                            |
| 15    | foi_isAdjourned     | Verdaagd     | Is de beslissing verdaagd (uitstel)?                                                             | Ja                                                                                                                    |
| 16    | foi_requester       | Verzoeker    | Informatie over de verzoeker, bijvoorbeeld 'Natuurlijk persoon' of 'Bedrijf X'                   | Natuurlijk persoon                                                                                                    |
| 17    | foi_requestText     | Verzoektekst | Korte tekst met het informatieverzoek.                                                           | Verzoeker vraagt om alle documenten die te maken hebben met de financiele situatie van de voetbalclub Zinkwegse Boys. |
| 18    | foi_decisionText    | Besluittekst | Korte tekst met het besluit.                                                                     | Er is op 5 mei 2022 besloten tot gedeeltelijke openbaarmaking.                                                        |
| 19    | foi_valuation       | Beoordeling  | Beoordeling ('deels openbaar', 'openbaar', 'niet openbaar', 'geen documenten', 'reeds openbaar') | Deels openbaar                                                                                                        |

## Voorbeelden
- [Lijst met Woo-dossiers van de gemeente Hoeksche Waard](https://doi.wooverheid.nl/?doi=nl.gm1963), of [diezelfde lijst in JSON](https://doi.wooverheid.nl/?doi=nl.gm1963&infobox=true)
- [Een specifiek dossier van de gemeente Hoeksche Waard](https://doi.wooverheid.nl/?doi=nl.gm1963.2i.2022.10), met rechts een infobox met metadata, of [datzelfde dossier weer in JSON](https://doi.wooverheid.nl/?doi=nl.gm1963.2i.2022.10&infobox=true)
