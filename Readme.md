# die Schrumpflationsapp

## So führen Sie das Projekt aus

### Repository klonen
Zuerst das Repository von GitHub klonen.

### Virtuelle Umgebung erstellen und aktivieren

```sh
python -m venv venv
```
Windows:
```sh
.\venv\Scripts\activate
```
macOS/Linux:
```sh
source venv/bin/activate
```

### Benötigte Pakete installieren
```sh
pip install -r requirements.txt
```

### Migrationen anwenden
```sh
python manage.py migrate
```

### Datenbank füllen
```sh
python manage.py populate_db
```

### Server starten
```sh
python manage.py runserver
```

### Anwendung aufrufen
Im Webbrowser http://127.0.0.1:8000/ aufrufen

