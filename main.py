from fastapi import FastAPI, HTTPException
from typing import List
import json
import os
from models import Reserva  # Importamos tu clase desde el otro archivo
app = FastAPI()
DATA_FILE = "reservas.json"
# Función para cargar datos del JSON al iniciar
def cargar_datos():
   if os.path.exists(DATA_FILE):
       with open(DATA_FILE, "r") as file:
           return json.load(file)
   return []
# Función para guardar datos en el JSON
def guardar_datos(datos):
   with open(DATA_FILE, "w") as file:
       json.dump(datos, file, indent=4)
# Inicializamos la lista con lo que haya en el archivo
reservas = cargar_datos()
@app.get("/")
def root():
   return {"message": "Sistema de reservas de salas (Persistente)"}
@app.post("/reservas")
def crear_reserva(reserva: Reserva):
   # Verificamos si el ID ya existe en la lista cargada
   for r in reservas:
       if r["id_reserva"] == reserva.id_reserva:
           raise HTTPException(status_code=400, detail="Ya existe una reserva con ese ID")
   # Agregamos a la lista y guardamos en el archivo
   nueva_reserva = reserva.model_dump()
   reservas.append(nueva_reserva)
   guardar_datos(reservas)
   return {"message": "Reserva registrada y guardada en JSON", "reserva": nueva_reserva}
@app.get("/reservas")
def obtener_reservas():
   return {"total": len(reservas), "reservas": reservas}