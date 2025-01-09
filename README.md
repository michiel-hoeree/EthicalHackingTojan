[github](https://github.com/michiel-hoeree/EthicalHackingTojan)


# module 1: enumeration en data storage
De eerste module dient ook als het controlescript. Dit script gebruikt een .env-bestand voor environment-variabelen. De eerste keer dat dit script wordt uitgevoerd op een computer, zal het een identifier maken voor de computer en een folder aanmaken in mijn GitHub-repository onder die naam. In deze folder staat een JSON-bestand dat nieuwe instructies kan geven aan het controlescript.

Wanneer het script opnieuw wordt uitgevoerd, zal het in zijn GitHub-folder controleren of er nieuwe modules moeten worden uitgevoerd. Als er een nieuwe module moet worden uitgevoerd, zal het de benodigde modules ophalen en uitvoeren.

Ik vond deze module een hele uitdaging, omdat ik meteen een aantal functionaliteiten werkend moest krijgen. Het werken met environment-variabelen was een nieuwe ervaring voor mij. Ik denk dat ik hier nog veel over te leren heb.

Na het afronden van mijn andere modules denk ik dat ik in deze module de environment-variabelen niet volledig volgens de best practices heb gebruikt. Het opslaan van een variabele voor de eerste uitvoering en mijn GitHub-token als environment-variabele is niet zoals het hoort. Ik hoop hier de volgende keer voorzichtiger mee te zijn.

Daarbij heb ik snel spijt gekregen van de manier waarop ik nieuwe modules uit voer. Door de nieuwe file uit te voeren in deze directory maar ze in een andere folder te schrijven was testen zeer moeilijk. Wanneer ik een nieuwe functionaliteit wou uittesten moest ik goed nakijken of de situaties in mijn modules folder hetzelfde zijn als in mijn root folder of ik moest dit script opnieuwe runnen wat nieuwe folders aanmakte in mijn root directory.



# module 2: reboot afleiding
Deze module zal eerst een lijst opstellen van alle apps die draaien en er één uit selecteren.
Als deze app een uur later nog draait, wordt de computer herstart. Als we na 10 uur nog niet hebben gereboot selecteren we een nieuwe runnende app.

Deze module is geïnspireerd door mijn eigen machine die, om onbekende redenen, af en toe crasht. Omdat ik nog geen patroon heb kunnen vinden, is dit heel moeilijk op te lossen, en ik hoop dit te kunnen nabootsen met deze module.

Ik had er echter niet aan gedacht dat dit ongelooflijk vervelend zou zijn om te testen en te demonstreren. Daarom heb ik de effectieve reboot vervangen door een simpele printfunctie en heb ik de reboot in commentaar gezet.

Daarnaast vond ik dit een interessante opdracht rond de processen op een computer. Eerst probeerde ik alle geïnstalleerde applicaties op te halen, maar deze worden in een volledig ander formaat weergegeven dan de draaiende processen. Daarom neem ik nu alleen de draaiende processen op.


# Module 3: ransomware
Deze module zal eerst proberen de encryptiesleutel uit het .env-bestand te halen. Als er nog geen encryptiesleutel is, wordt er een aangemaakt, opgeslagen en worden bestanden op de computer met een specifieke extensie versleuteld. Hierna kun je de gebruiker afpersen om de bestanden te ontsleutelen.

Dit was de laatste module die ik schreef. Ik vond dit een zeer moeilijke module om veilig te maken. Omdat deze module alle bestanden op je computer kan versleutelen en de sleutel verloren kan gaan als je deze niet zorgvuldig opslaat, was er een risico dat ik dit script per ongeluk op mijn eigen computer zou uitvoeren. Daarom zorgde ik ervoor dat dit script op dit moment alleen bestanden in één specifieke map op je computer zal versleutelen. Deze map kun je zelf instellen.

Bij het schrijven van dit script leerde ik snel dat ik zorgvuldiger moet omgaan met mijn globale variabelen en hoe ik moet opslaans.