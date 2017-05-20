# douwes-beschikbaar
Een Python script om te kijken of een boek leverbaar is op boekhandeldouwes.nl,
aan de hand van een ISBN en/of een titel, via gebruikersinput of een .csv bestand.

Inclusief een tkinter grafische gebruikersinterface.

# Gebruik

Voor het gebruik van dit programma heb je een .csv bestand nodig met ISBNs en
de bijbehorende boektitels in het volgende formaat:

```
ISBN,titel
ISBN,"titel met spaties
```

Het pad naar dit bestand moet gedefiniëerd worden in de "book_file" variabele.

## douwes_beschikbaar.py

```
douwes_beschikbaar.py ISBN
```

Als je geen ISBN specifiëerd in je programma-aanroep, zal het programma je vragen
er een op te geven.

## douwes_beschikbaar_gui.py

Voer het programma uit, vul een ISBN in en klik op "zoeken". Binnen niet al te
lange tijd zal er staan of het ISBN leverbaar is.
