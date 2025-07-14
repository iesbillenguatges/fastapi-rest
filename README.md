
# Gestor de Tasques amb FastAPI + HTML/JS a derplegar en render.com

Aquest projecte és una aplicació molt senzilla però completa que mostra com utilitzar **FastAPI** (un microframework modern i ràpid per a APIs) juntament amb **HTML + JavaScript** per crear una eina de gestió de tasques.

## Tecnologies utilitzades
- **Python 3**
- **FastAPI**
- **Uvicorn**
- **HTML + JavaScript**
- **Fetch API**
- **Render.com** per desplegar

## Estructura
```
main.py
requirements.txt
static/index.html
```

## Execució local
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
Obri [http://localhost:8000](http://localhost:8000) al navegador.

## Render.com
Start Command:
```
uvicorn main:app --host 0.0.0.0 --port 10000
```

El `index.html` es servirà automàticament a `/`.

## ✨ Funcions
- Afegir / esborrar / completar tasques
- Interfície dinàmica amb JavaScript
- Backend RESTful amb FastAPI

## Utilitat
Ideal per aprendre com crear i desplegar aplicacions modernes basades en APIs i frontend senzills.
