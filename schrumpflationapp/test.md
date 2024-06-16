# ESA 3 Schrumpflations-App Design
* Formatierungshinweise für .md: https://www.freecodecamp.org/news/how-to-use-markdown-in-vscode/

## urls.py
* path start/
* path produkteingabe/
* path produktliste/
* path supermarktergänzen/

## settings.py
* INSTALLED_APPS
    + schrumpflation
    + bootstrap4

## Views
* def get_kaufobjekt_list
* def add_kaufobjekt
* def add_supermarkt
* def add_produkt

## Models
* class Supermarkt
    + Kette
    + Straße
    + Hausnummer
    + PLZ
    + Stadt
    + Öffnungszeiten
* class Produkt
    + Art
    + Marke
* class Kaufobjekt
    + Produkt
    + Supermarkt
    + Größe
    + Preis
    + Datum

## Template/HTML
*  

## Tags & Filter


## Forms
* ProduktForm