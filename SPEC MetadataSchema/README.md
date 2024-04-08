# Woogle metadata specificatie
Versie 2.0 - Universiteit van Amsterdam - Maik Larooij, Maarten Marx

- [Woo-basis metadata](#woo-basis)
    * [Attributen](#attributen)
    * [Verplichtingen](#verplichtingen)
- [Categorie-specifieke metadata](#categorie-specifieke-metadata)
    * [Nieuwsberichten (categorie 1b-n)](#nieuwsberichten--categorie-1b-n-)
    * [Toespraken (categorie 1b-t)](#toespraken--categorie-1b-t-)
    * [Bereikbaarheidsgegevens (categorie 1e)](#bereikbaarheidsgegevens--categorie-1e-)
    * [Verwijsindex (categorie 1e-i)](#verwijsindex--categorie-1e-i-)
    * [Vergaderstukken Staten-Generaal (categorie 2b)](#vergaderstukken-staten-generaal--categorie-2b-)
    * [Agenda/besluitenlijst (categorie 2d)](#agenda-besluitenlijst--categorie-2d-)
    * [Adviezen (categorie 2e)](#adviezen--categorie-2e-)
    * [Advies: beslisnota (categorie 2e-b)](#advies--beslisnota--categorie-2e-b-)
    * [Convenanten (2f)](#convenanten--2f-)
    * [Woo/Wob-verzoeken (categorie 2i)](#woo-wob-verzoeken--categorie-2i-)
    * [Onderzoeken (categorie 2j)](#onderzoeken--categorie-2j-)
    * [Beschikkingen (categorie 2k)](#beschikkingen--categorie-2k-)
- [Woo-basis voor losse documenten](#woo-basis-voor-losse-documenten)
- [Voorbeelden](#voorbeelden)

We hebben te maken met verschillende informatiecategorieën die vallen onder de Woo. Toch is het belangrijk om deze categorieën op enigzins dezelfde wijze op te slaan, om bijvoorbeeld:
- Tegelijkertijd te kunnen zoeken in alle openbaar gemaakte stukken, bijvoorbeeld resultaten uit convenanten en Woo-verzoeken;
- Te kunnen groeperen op thema, om alle openbaar gemaakte stukken behorend aan een bepaald thema te kunnen doorzoeken;
- Het mogelijk te maken om de groepering anders te laten zijn voor burgers, journalisten of andere nuttigers, bijvoorbeeld het ordenen van een website op thema in plaats van op informatiecategorie. 

De attributen hebben bij ons ook een prefix om aan te geven waar ze vandaan komen:
- [dc -> Dublin Core](https://www.dublincore.org/)
- tooiwl -> TOOI voor themaindeling
- foaf -> Friend of a Friend, een standaard voor het beschrijven van personen en organisaties
- foi -> Freedom of Information, onze eigen namespace voor attributen die niet bestaan in een gangbare standaard

## Woo-basis
De volgende attributen kunnen worden ingezet voor elke informatiecategorie. Deze maken het mogelijk om alle openbaar gemaakte stukken toch met elkaar te kunnen matchen op bijvoorbeeld aanbieder, jaar/publicatiedatum of thema.

### Attributen
| **#** | **Technische naam** | **Naam**            | **Omschrijving**                                                                                                                                                                                              | **Voorbeeld**                                                                                                                                                |
|-------|---------------------|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|                                              
| 1     | dc_title            | Titel               | Titel van het stuk.                                                                                                                                                                                           | Woo-verzoek over voetbalvereniging Zinkwegse Boys (HSW)                                                                                                      |
| 2     | dc_description      | Beschrijving        | Beschrijving van het stuk.                                                                                                                                                                                    | Verzoeker vraagt om informatie over de aanleg van speelvoorzieningen, extra kleedkamers, vergroting van het parkeerterrein en een gesprek met een omwonende. |
| 3     | dc_publisher        | Aanbieder           | De aanbieder van het stuk, in de vorm van een TOOI code, zie bijvoorbeeld [hier](https://tardis.overheid.nl/waardelijst?work_uri=https%3A%2F%2Fidentifier.overheid.nl%2Ftooi%2Fset%2Frwc_gemeenten_compleet). | `gm1963`                                                                                                                                                     |
| 4     | foi_publishedDate   | Publicatiedatum     | De datum van publicatie van het stuk (YYYY-mm-dd).                                                                                                                                                            | 2022-08-23                                                                                                                                                   |
| 5     | dc_date_year        | Jaar                | Kan worden afgeleid van publicatiedatum of zelf worden ingevuld als minimale eis aan iets van een datum.                                                                                                      | 2022                                                                                                                                                         |
| 6     | tooiwl_topic        | Thema/onderwerp     | Het thema of onderwerp behorend aan het openbaar gemaakte stuk.                                                                                                                                               | ruimte en infrastructuur                                                                                                                                     |
| 7     | dc_type             | Informatiecategorie | De informatiecategorie in de vorm van de wetcode, bijvoorbeeld `2i` voor Woo-verzoeken en `2f` voor convenanten.                                                                                              | `2i`                                                                                                                                                         |
| 8     | dc_source           | Bron (URL)          | De URL waar het stuk kan worden gevonden.                                                                                                                                                                     | https://openpub.gemeentehw.nl/..........                                                                                                                     |
| 9    | dc_creator          | Maker               | Maker van de publicatie in onze database (meestal ook de TOOI code, of bijvoorbeeld een Scraper-versie).                                                                                                      | `gm1963`                                                                                                                                                                                                                                                                                           |
| 10    | foi_linkedDossier   | Gelinkt dossier     | Eerste aanzet tot het mogelijk maken van 'linken' van dossier, bijvoorbeeld deelbesluiten. Waarde is dan de identifier van het gelinkte dossier.                                                              | `nl.gm1963.2i.2022.11`                                                                                                                                       |
| 11    | foi_files  | Documenten   | Lijst met documenten volgens [specificatie](#woo-basis-voor-losse-documenten).                                                               | `nl.gm1963.2i.2022.11.1`                                                                                                                                     |

### Verplichtingen
Voor onze doeleinden verplichten wij bij het insturen enkel de volgende velden:
- Titel (dc_title)
- Informatiecategorie (dc_type)
- Aanbieder (dc_publisher)
- Een vorm van een datum, minimaal het jaar (dc_date_year)
- Een ID (dc_identifier) genereren wij zelf


## Categorie-specifieke metadata
Deze hebben we nu enkel samengesteld voor de categorie 'Woo/Wob-verzoeken'. De stukken bevatten dus de velden zoals genoemd in de Woo-basis, plus deze velden:

### Nieuwsberichten (categorie 1b-n)
**Geen extra velden**

### Toespraken (categorie 1b-t)
**Geen extra velden**

### Bereikbaarheidsgegevens (categorie 1e)
| **#** | **Technische naam** | **Naam**            | **Omschrijving**                                                                | **Voorbeeld**                                                    |
|-------|---------------------|---------------------|---------------------------------------------------------------------------------|------------------------------------------------------------------|
| 1     | foaf_initials       | Initialen           | Initialen van de persoon.                                                       | L.T.                                                             |
| 2     | foaf_name           | Volledige naam      | Volledige naam van de persoon/organisatie.                                      | Mark Rutte                                                       |
| 3     | foaf_firstName      | Voornaam            | Voornaam van de persoon.                                                        | Mark                                                             |
| 4     | foaf_lastName       | Achternaam          | Volledige achternaam van de persoon.                                            | Rutte                                                            |
| 5     | foaf_mbox           | E-mail adres        | E-mail adres van persoon/organisatie.                                           | mark@rutte.nl                                                    |
| 6     | foaf_phone          | Telefoonnummer      | Telefoonnummer van persoon/organisatie.                                         | +31 02912839                                                     |
| 7     | foaf_img            | Link naar foto      | Link naar foto, bijvoorbeeld pasfoto.                                           | https://www.rijksoverheid.nl/.../mark-rutte-5.jpg                |
| 8     | foi_city            | Woonplaats          | Woonplaats/stad van persoon/organisatie.                                        | Den Haag                                                         |
| 9     | foi_startDate       | Startdatum          | Startdatum persoon/organisatie                                                  | 2010-10-14                                                       |
| 10    | foi_endDate         | Einddatum           | Einddatum persoon/organisatie                                                   | 2023-12-05                                                       |
| 11    | foi_partyName       | Partijnaam          | Naam partij waar persoon lid van is.                                            | VVD                                                              |
| 12    | foi_function        | Functie             | Functie van de persoon (code).                                                  | 8012                                                             |
| 13    | foi_rawFunction     | Functienaam         | Functie van de persoon (verkegen naam).                                         | Minister-president                                               |
| 14    | foaf_homepage       | Webpagina           | Webpagina van de persoon/organisatie.                                           | https://www.rijksoverheid.nl/regering/bewindspersonen/mark-rutte |
| 15    | foi_linkedin        | LinkedIn            | LinkedIn link van de persoon/organisatie. | https://www.linkedin.com/in/mark-rutte                           |
| 16    | foi_twitter         | Twitter             | Twitter link van de persoon/organisatie.                                        | https://www.twitter.com/minpres                                  |
| 17    | foi_wikipedia       | Wikipedia           | Wikipedia link van de persoon/organisatie.                                      | https://www.wikipedia.nl/wiki/Mark_Rutte                         |
| 18    | foi_fax             | Faxadres            | Faxadres van de persoon/organisatie.                                            |                                                                  |
| 19    | foi_mailAddress     | Postadres           | Postadres van de persoon/organisatie.                                           |                                                                  |
| 20    | foi_visitAddress    | Bezoekadres         | Bezoekadres van de persoon/organisatie.                                         |                                                                  |
| 21    | foi_academicTitle   | (academische) Titel | (academische) Titel van de persoon.                                             | dhr. drs.                                                        |
| 22    | foi_active          | Actief              | Geeft aan of the persoon/organisatie nog steeds actief is.                      | True                                                             |
| 23    | foi_updateDate      | Updatedatum         | Datum van laatste update gegevens.                                              | 2023-12-05                                                       |

### Verwijsindex (categorie 1e-i)
| **#** | **Technische naam** | **Naam**     | **Omschrijving**                                                                                 | **Voorbeeld**                                                                                                         |
|-------|---------------------|--------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 1    | foi_updateDate    | Datum update gegevens | Datum van de laatste update van de gegevens                                                  | 2023-12-05                                                                                                          |

### Vergaderstukken Staten-Generaal (categorie 2b)
| **#** | **Technische naam** | **Naam**     | **Omschrijving**                                                                                 | **Voorbeeld**                                                                                                         |
|-------|---------------------|--------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 1    | foi_identifierSuffix    | Suffix voor identifier | Kan worden gebruikt om handmatig het laatste deel van de identifier in te voegen.                                                | 19-21                                                                                                         |
| 2    | dc_externalIdentifier    | Externe identifier | Identifier gebruikt door externe partij                                                | h-tk-20232024-25-15                                                                                                         |
| 3 | foi_meetingYear | Vergaderjaar | Vergaderjaar van de vergadering | 2023-2024 |
| 4 | foi_meetingDate | Vergaderdatum | Datum van de vergadering | 2023-12-05 |
| 5 | foi_meetingNumber | Vergadernummer | Nummer van de vergadering | 25 |
| 6 | foi_meetingItemNumber | Agendapuntnummer | Nummer van het agendapunt | 15 |
| 7 | foi_handelingType | Handelingtype | Type handeling, bijvoorbeeld 'Stemmingen', 'Plenair debat' | Stemmingen |
| 8 | foi_startPage | Startpagina | Startpagina van het document (voor oudere handelingen) | 301 |
| 9 | foi_endPage | Eindpagina | Eindpagina van het document (voor oudere handelingen) | 305 |


### Agenda/besluitenlijst (categorie 2d)
| **#** | **Technische naam** | **Naam**     | **Omschrijving**                                                                                 | **Voorbeeld**                                                                                                         |
|-------|---------------------|--------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 1    | foi_decisionDate    | Besluitdatum | Datum van besluit op agenda/lijst.                                                | 2023-12-05                                                                                                          |

### Adviezen (categorie 2e)
| **#** | **Technische naam** | **Naam**     | **Omschrijving**                                                                                 | **Voorbeeld**                                                                                                         |
|-------|---------------------|--------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 1    | foi_decisionDate    | Besluitdatum | Datum van besluit op advies.                                              | 2023-12-05                                                                                                          |

### Advies: beslisnota (categorie 2e-b)
| **#** | **Technische naam** | **Naam**     | **Omschrijving**                                                                                 | **Voorbeeld**                                                                                                         |
|-------|---------------------|--------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 1    | foi_decisionDate    | Besluitdatum | Datum van besluit op beslisnota.                                         | 2023-12-05                                                                                                          |

### Convenanten (2f)
| **#** | **Technische naam** | **Naam**     | **Omschrijving**                                                                                 | **Voorbeeld**                                                                                                         |
|-------|---------------------|--------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 1    | foi_decisionDate    | Besluitdatum | Datum van besluit op convenant.                                               | 2023-12-05                                                                                                          |


### Woo/Wob-verzoeken (categorie 2i)
| **#** | **Technische naam** | **Naam**     | **Omschrijving**                                                                                 | **Voorbeeld**                                                                                                         |
|-------|---------------------|--------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 1    | foi_requestDate     | Verzoekdatum | Datum van het Wob/Woo-verzoek.                                                                   | 2022-04-12                                                                                                            |
| 2    | foi_decisionDate    | Besluitdatum | Datum van het besluit op het Wob/Woo-verzoek                                                     | 2022-05-01                                                                                                            |
| 3    | foi_isAdjourned     | Verdaagd     | Is de beslissing verdaagd (uitstel)?                                                             | Ja                                                                                                                    |
| 4    | foi_requester       | Verzoeker    | Informatie over de verzoeker, bijvoorbeeld 'Natuurlijk persoon' of 'Bedrijf X'                   | Natuurlijk persoon                                                                                                    |
| 5    | foi_requestText     | Verzoektekst | Korte tekst met het informatieverzoek.                                                           | Verzoeker vraagt om alle documenten die te maken hebben met de financiele situatie van de voetbalclub Zinkwegse Boys. |
| 6    | foi_decisionText    | Besluittekst | Korte tekst met het besluit.                                                                     | Er is op 5 mei 2022 besloten tot gedeeltelijke openbaarmaking.                                                        |
| 7    | foi_valuation       | Beoordeling  | Beoordeling ('deels openbaar', 'openbaar', 'niet openbaar', 'geen documenten', 'reeds openbaar') | Deels openbaar                                                                                                        |

### Onderzoeken (categorie 2j)
| **#** | **Technische naam** | **Naam**     | **Omschrijving**                                                                                 | **Voorbeeld**                                                                                                         |
|-------|---------------------|--------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 1    | foi_decisionDate    | Besluitdatum | Datum van besluit op onderzoek.                                              | 2023-12-05                                                                                                          |


### Beschikkingen (categorie 2k)
| **#** | **Technische naam** | **Naam**     | **Omschrijving**                                                                                 | **Voorbeeld**                                                                                                         |
|-------|---------------------|--------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 1    | foi_geoInfo    | Geografische info | Geografische info in JSON, bijvoorbeeld coordinaten van het betreffende gebied.                                                  | [{"kml_Point": "POINT(234558.331 582660.491)"....... }]                                                                                                           |
| 2    | foi_startDate    | Startdatum | Startdatum van ingaan beschikking (YYYY-MM-dd)                                                                    | 2023-12-05                                                        |
| 3    | foi_endDate    | Einddatum | Einddatum van beschikking (YYYY-MM-dd)                                                                    | 2024-12-05                                                        |
| 4    | foi_subjectAddress    | Betreffende adres | Adres betreffende beschikking.                                                                 | Eerste Veldweg 1, 9501LH, Stadskanaal, Gemeente Stadskanaal                                                        |
| 5    | foi_subjectCoordinates    | Betreffende coordinaten | Coordinaten betreffende beschikking.                                                               | (6.754141691849271, 53.15091900160704)                                             |

## Woo-basis voor losse documenten
| **#** | **Technische naam** | **Naam**        | **Omschrijving**                                                                                  | **Voorbeeld**                            |
|-------|---------------------|-----------------|---------------------------------------------------------------------------------------------------|------------------------------------------|
| 1     | dc_title            | Titel           | Titel van het document.                                                                           | Besluitbrief Woo Geredigeerd             |
| 2     | dc_source           | Bron (URL)      | URL naar het document.                                                                            | https://openpub.gemeentehw.nl/.......... |
| 3     | dc_type             | Type document   | Type van het document, bijvoorbeeld 'bijlage', 'besluit', 'inventarislijst'.                      | besluit                                  |
| 4 | foi_documentType | Documenttype | Type van het document op een lager niveau, bijvoorbeeld 'email', 'brief' | email |
| 5     | foi_sentDate        | Datum           | Datum van verzenden of aanmaken document                                                          | 2022-07-21                               |
| 6     | foi_originator      | Verzender       | Verzender van het document.                                                                       | Burgemeester.....                        |
| 7     | foi_recipient       | Ontvanger       | Ontvanger van het document                                                                        | Raadslid.....                            |
| 8     | foi_url_on_web      | Op het web?     | Staat het document op het web?                                                                    | True                                     |
| 9     | dc_description      | Beschrijving    | Beschrijving van het document.                                                                     | Reactie minister op brief van 2023-01-20                                     |
| 10 | foi_groundsOfRefusal | Weigeringsgronden | Weigeringsgronden van het document (wetcode) | 2.1.e |
| 11 | foi_valuation | Beoordeling | Beoordeling ('deels openbaar', 'openbaar', 'niet openbaar', 'reeds openbaar') | Deels openbaar |

Verder zijn er nog een aantal attributen die wij voor onze eigen doeleinden ophalen uit de documenten, zoals de tekst, tekst na OCR, aantal woorden, aantal karakters etcetera.

### Verplichtingen
Voor documenten is niet zoveel verplicht, we willen in ieder geval de URL hebben om hem op te halen (dc_source). Hier halen we zelf al veel uit. Een ID (dc_identifier) genereren we zelf.
- URL (dc_source)
- Staat de URL op het web? (foi_url_on_web)

## Voorbeelden
- [Lijst met Woo-dossiers van de gemeente Hoeksche Waard](https://doi.wooverheid.nl/?doi=nl.gm1963), of [diezelfde lijst in JSON](https://doi.wooverheid.nl/?doi=nl.gm1963&infobox=true)
- [Een specifiek dossier van de gemeente Hoeksche Waard](https://doi.wooverheid.nl/?doi=nl.gm1963.2i.2022.10), met rechts een infobox met metadata, of [datzelfde dossier weer in JSON](https://doi.wooverheid.nl/?doi=nl.gm1963.2i.2022.10&infobox=true)
