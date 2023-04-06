# Woogle API beschrijving

Met de Woogle API stuur je *Woo dossiers* naar de Woogle database, waarna die vervolgens in de Woogle zoekmachine terecht komen. 

Je stuurt de informatie in `JSON` formaat. Een Woo-dossier bestaat in de regel uit een verzoek, een besluit, een inventarislijst en een stel vrijgegeven documenten. De API ondersteunt zowel het verwerken van losse dossiers als het verwerken van een lijst van dossiers.

Niet elk Woo dossier is hetzelfde en ook zijn er niet voor elk Woo dossier dezelfde bestanden en gegevens beschikbaar. Toch kan vrijwel elk Woo-dossier via de API *geupload* worden.

## OpenWebConcept

Als eerste optie kunt u kijken naar [OpenWebConcept](https://openwebconcept.nl/). Gemeentes die hierbij zijn aangesloten hebben zowel publicaties op de eigen pagina (bijvoorbeeld [deze](https://www.gemeentehw.nl/openwoo/woo-verzoek-over-de-laan-van-heemstede/b8521336-476d-42e5-821d-a2d0eb7626b7)) als door middel van een [API](https://openpub.gemeentehw.nl/wp-json/owc/openwoo/v1/items) voor verdere verwerking. Er is al veel enthousiasme; deze week verscheen er een bericht in het Binnenlands Bestuur over de [goede kwaliteit van de dossiers van de Gemeente Hoeksche Waard](https://www.binnenlandsbestuur.nl/digitaal/expert-roemt-kwaliteit-van-door-gemeente-gepubliceerde-woo-verzoeken). Wij hebben een rechtstreekse verbinding met deze gemeenten, en publicaties komen daardoor direct terecht in Woogle, win-win!

## Het model

Het idee achter een Woo-dossier is eenvoudig, en het JSON model volgt dat. Een Woo-dossier bestaat uit

1. wat gegevens over het dossier, een titel, de naam/code van het bestuursorgaan, etc
2. documenten, met per document altijd een url waar het document opgehaald kan worden en eventueel wat gegevens over het document.

## Het uploaden van documenten

In de JSON beschrijving van een dossier staan dus die gegevens, en voor elk document een URL waar het opgehaald kan worden. Dat kan een blijvende URL op het web zijn, maar ook een tijdelijke die alleen voor het upload proces gemaakt is. 

Het uploaden kan gaan via een zip bestand met daarin de losse documenten, of via losse documenten en URLs. 

De volgende document types kunnen verwerkt worden. We gaan ervan uit dat de file-extensies correct zijn. 

* `.zip` 
* `.pdf`
* `.csv` (echt ook comma gescheiden) en `.xls` en `.xlsx`
* `.html`
* `.txt`

## Het absolute minimum

Er kan flink wat over een dossier en de documenten gezegd worden, maar dat hoeft niet. Er is maar heel weinig verplicht. Het minimale JSON bestand ziet er als volgt uit en is ook te vinden in [woo_dossier_absoluut_minimum.json](woo_dossier_absoluut_minimum.json):

```
[
    { 
        "dc_title": "Woo verzoek Asfaltcentrale",
        "dc_description": "Naar aanleiding van een verzoek op grond van de Wet open overheid (Woo) om openbaarmaking van informatie omtrent asfaltcentrale aan de Asfaltstraat 13 te Lelystad, heeft het college besloten de gevraagde informatie, voor zover aanwezig, gedeeltelijk openbaar te maken.",
        "dc_publisher": "pv24",
        "dc_date_year": 2022,
        "dc_type": "2i",
        "foi_files": {
            "foi_documenten": [ 
                {
                    "dc_source": "WAARDE: Hyperlink naar zip of pdf bestand",
                    "foi_url_on_web": "WAARDE: Als bestand op het web blijft staan: True. Anders: False. Default bij niet invullen: False.  "
                }
            ]
        }
    }
]

```
Hier gaan de eerste 5 `dc_` velden over het dossier. Waarbij `dc_publisher` iets zegt over de publiceerder van het dossier en `dc_type` bij Woo-dossiers altijd gelijk is aan `2i`.
Vanzelfsprekend moet `dc_date_year` een valide jaartal zijn. 
De waarde voor `dc_publisher` is de zogenaamde   *tooiont:organisatie code*. Bijvoorbeeld  `pv24`  voor de Provincie Flevoland.  Deze waardes zijn te vinden op <https://tardis.overheid.nl/waardelijsten.html> en daarin de lijsten *Register XXX compleet*, voor XXX gemeentes, provincies, ministeries, waterschappen, etc.",

Hier is gekozen om één pdf of zip bestand te uploaden waarover verder niks meer gespecificeerd wordt. Het attribuut `"foi_url_on_web"` geeft aan of dat bestand op die URL beschikbaar blijft of niet (default is dus niet).


## Extra informatie over het dossier

In het voorbeeld [woo_dossier_fair.json](woo_dossier_fair.json) zijn een aantal extra velden opgenomen die eigenlijk altijd wel bekend zijn voor een Woo-dossier, omdat ze in het besluit staan. Nu staan ze hier ook expliciet, zodat ze mooi op een pubicatie site meegenomen kunnen worden, en gebruikt worden om beter te kunnen zoeken. Als er een verzoeks of besuit datum wordt gegeven, hoeft vanzelfsprekend het `dc_date_year` attribuut niet meer ingevuld te worden (dit mag wel). Datums zijn altijd ISO-datums `yyyy-mm-dd`. 
Het optionele veld `dc_source` bevat een url die verwijst naar een webpagina over dit dossier.
Het veld `foi_linkedDossier` maakt het mogelijk om een dossier te koppelen aan een bestaand dossier, bijvoorbeeld als het gaat om een vervolgbesluit. Gebruik hiervoor de DOI van een bestaand dossier.
Hier staat een voorbeeld

```
"dc_source": "WAARDE: hyperlink naar webpagina over dit dossier",
"foi_requestDate": "2022-08-11",
"foi_decisionDate": "2022-09-27",
"foi_requestText": "U verzoek, kort samengevat, openbaarmaking van Informatie met betrekking tot toezicht en handhaving asfaltcentrale aan de Asfaltstraat 13 te Lelystad.",
"foi_decisionText": "Wij besluiten de door u gevraagde informatie (gedeeltelijk) openbaar te maken. Voor een nadere specificatie per documenten verwijzen wij u naar de inventarislijst en de documenten.",
"foi_linkedDossier": "nl.gmxxxx.2i.2022.1"
```    

## De documenten los

In het voorbeeld [woo_dossier_fair.json](woo_dossier_fair.json) zien we ook hoe de verschillende soorten documenten apart vermeld kunnen worden. Als het verzoek, het besluit of inventarislijst apart vermeld worden, worden die ook zo benoemd op de publicatie pagina en in Woogle.  Men kan dan ook gericht zoeken naar informatie die voorkomt in het besluit bijvoorbeeld. 

Het is mogelijk om per document een titel mee te geven. Wordt dit niet gedaan, dan wordt de filenaam in Woogle gebruikt ter presentatie.

Net als eerder, geeft `"foi_url_on_web"` weer aan of het document blijvend op deze URL te vinden is. 

Het attribuut `"foi_documenten"` is bijzonder omdat dit een *lijst* waarde heeft. We kunnen er dus meerdere documenten instoppen. Maar natuurlijk ook gewoon 1 zip bestand. 

Het voordeel van het los aangeven van alle vrijgegeven documenten is dat de gegevens per document die meestal in de inventarislijst staan nu ook per document als metadata kunnen worden meegegeven. Hier staat een voorbeeld van de mogelijkheden voor 1 document:

```
{
    "dc_title": "Email n.a.v. Asfaltcentrale",
    "dc_source": "https://www.flevoland.nl/getmedia/0c03a913-730c-4644-9ecd-e6b24604d165/Woo-verzoek-Asfaltcentrale-documenten.pdf", 
    "foi_url_on_web":"True",
    "dc_description": "Email gestuurd over werkzaamheden aan de asfaltcentrale",
    "foi_sentDate": "2022-06-12",
    "foi_documentType": "Email",
    "foi_valuation": "Deels openbaar",
    "foi_groundsOfRefusal": "5.1.e; 5.1.f",
    "foi_originator": "Raadslid van Dijk",
    "foi_recipient": "Raadslid Jansen"
}
``` 
Hierin moet `"foi_groundsOfRefusal"` een `;` gescheiden lijst van weigeringsgronden zijn.

## Upload proces

Het uploaden van één of meerdere dossiers kan door te praten met de API door middel van een `HTTP POST request`. We bespreken de twee simpelste manieren om dit te doen.

Gebruik bij het uploaden de volgende gegevens:
- URL: https://api.wooverheid.nl
- Authenticatie: Basic Auth (gebruikersnaam + wachtwoord)
- Body: een valide JSON

Uploaden kan via de command-line tool curl, en daarvoor is een gebruikersnaam en wachtwoord nodig. Met het volgende commando kan er een dossier worden opgestuurd dat staat opgeslagen in `test.json`:

`curl -XPOST -H "Content-Type: application/json" --data-binary @test.json https://api.wooverheid.nl -u USERNAME`

Er verschijnt dan een prompt om een wachtwoord in te voeren. Als de gegevenscombinatie juist is zal het verzoek in behandeling worden genomen.
Ook via tools als [Postman](https://www.postman.com/) kan er een POST request worden gedaan. Als authenticatie type dient 'Basic Auth' te worden gekozen. 

### Uploaden: invoeren met behulp van een simpele interface

Een tweede mogelijkheid is om een dossier te uploaden via https://upload.wooverheid.nl. Hier kan worden ingelogd met dezelfde gebruikersnaam/wachtwoord combinatie. In het hoofdmenu kan op 'Nieuw dossier' worden geklikt om een nieuw dossier te maken. Vul de gegevens over het dossier in en voeg de bijbehorende bestanden onderaan toe.

![woofairify](woofairify.png)

Controleer na het maken van het dossier de gegevens en klik op 'verzenden' om het dossier op te sturen.

### Dossiers verwijderen of aanpassen

Een dossier aanpassen of verwijderen kan zowel via https://upload.wooverheid.nl als via de API. Op de uploadsite staan op het beginscherm knoppen die je door het proces leiden. Voor de API zijn de volgende commando's handig:

`curl -XDELETE https://api.wooverheid.nl/nl.test.2i.2022.1 -u USERNAME` om een dossier (met identifier `nl.test.2i.2022.1`) te verwijderen.

`curl -XPATCH -H "Content-Type: application/json" --data-binary @update.json https://api.wooverheid.nl -u USERNAME` om dossiers aan te passen. `update.json` ziet er dan bijvoorbeeld zo uit:

```
{
    "dc_identifier": "nl.test.2i.2022.1",
    "dc_description": "Nieuwe beschrijving!",
    "foi_decisionDate": "2022-01-01",
    "foi_requestDate": ""
}
```

Elk dossier dat aangepast dient te worden moet zijn voorzien van een identifier. De rest van de velden zijn hetzelfde als bij het uploaden van een nieuw dossier. In het voorbeeld worden de beschrijving en besluitdatum aangepast/toegevoegd en de verzoekdatum juist weggehaald. Als het dossier na aanpassing niet meer voldoet aan de minimale standaard (zie "Het absolute minimum") zal de aanpassing niet worden doorgevoerd en zullen er foutmeldingen in beeld komen die helpen bij het oplossen.

### Validatie en foutmeldingen

Na uploaden/aanpassen/verwijderen van een dossier gebeuren er meestal 2 dingen:

1. Het json bestand wordt gevalideerd. Staan alle verplichte velden erin en kloppen de datatypes. 
    *  De json mag velden bevatten die niet beginnen met de namespaces `dc_` of `foi_`. Wij doen daar dan niets mee. Dit kan handig zijn voor commentaar of wat dan ook. 
    *  De volgorde van de attributen is volkomen vrij. 
2. We kijken of de urls geen foutmelding geven.

Als alles goed is, krijg je een OK terug. Zo niet, dan een foutmelding waarin is aangegeven wat er mis is gegaan. Hieronder staat een voorbeeld van een reactie op een ongeldige inzending.

```
{
   "host": "api.wooverheid",
   "status": 400,
   "status_text": "Bad Request",
   "request_type": "POST",
   "success": false,
   "errors": [
      "Error in dossier 1: please provide a 'dc_title' for every dossier!",
      "Error in dossier 1: test_publisher is an invalid publisher!",
      "Error in dossier 2 - foi_besluit: please provide a 'dc_source' for every document!",
      "Error in dossier 3 - document 1: 'foi_invalid' is not a valid attribute for an attached document!"
   ]
}
```

Na deze melding kan het nog even duren voordat het dossier volledig is verwerkt en zichtbaar is in Woogle.

