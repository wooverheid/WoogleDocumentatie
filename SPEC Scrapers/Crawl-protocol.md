# Crawl-protocol Woogle

## Webscrapers
Alle webscrapers werken min of meer volgens de volgende logica:
1. De scraper haalt alle links op naar losse dossiers van dit bestuursorgaan.
2. De links worden gefilterd op basis van de URL. Als de URL al bekend is in onze database, dan wordt deze overgeslagen. Dit betekent ook dat wijzigingen achteraf in bij ons bekende dossiers **niet** worden doorgevoerd. Ook worden ze niet verwijderd als ze niet meer op de bron website staan. De bereikbaarheidsgegevens (1e) en index (1e-i) worden **wel** bijgewerkt als er nieuwe informatie is.
3. Voor elk overgebleven individueel dossier wordt de metadata opgehaald.
4. De scraper produceert een lijst met dossiers en metadata in JSON formaat, die vervolgens kan worden geupload naar onze database.

## API's
We zijn aangesloten op een aantal API's. Deze werken min of meer volgens de volgende logica:
1. De API wordt aangeroepen om alle dossiers van dit/deze bestuursorgaan/bestuursorganen op te halen.
2. De gevonden dossiers worden vertaald naar een formaat dat wij kunnen verwerken. Dat betekent het koppelen van de attribuutnamen van de API aan de attribuutnamen van Woogle.
3. De dossiers worden gefilterd op basis van de URL. Als de URL al bekend is in onze database, dan wordt deze overgeslagen. Dit betekent ook dat wijzigingen achteraf in bij ons bekende dossiers **niet** worden doorgevoerd. Ook worden ze niet verwijderd als ze niet meer op de bron website staan.
4. De API produceert een lijst met dossiers en metadata in JSON formaat, die vervolgens kan worden geupload naar onze database.
