
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def llegir_arrel():
    return FileResponse("static/index.html")

class Tasca(BaseModel):
    id: int
    titol: str
    completada: bool = False

tasques: List[Tasca] = []

@app.get("/tasques")
def llistar_tasques():
    return tasques

@app.get("/tasques/{id}")
def obtenir_tasca(id: int):
    for tasca in tasques:
        if tasca.id == id:
            return tasca
    raise HTTPException(status_code=404, detail="Tasca no trobada")

@app.post("/tasques")
def afegir_tasca(tasca: Tasca):
    tasques.append(tasca)
    return tasca

@app.put("/tasques/{id}")
def actualitzar_tasca(id: int, nova_tasca: Tasca):
    for i, t in enumerate(tasques):
        if t.id == id:
            tasques[i] = nova_tasca
            return nova_tasca
    raise HTTPException(status_code=404, detail="Tasca no trobada")

@app.delete("/tasques/{id}")
def eliminar_tasca(id: int):
    for i, t in enumerate(tasques):
        if t.id == id:
            del tasques[i]
            return {"missatge": "Tasca eliminada"}
    raise HTTPException(status_code=404, detail="Tasca no trobada")
