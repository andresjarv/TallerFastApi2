from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

reservas: List[dict] = []


class Reserva(BaseModel):
    id_reserva: int
    id_sala: int
    id_usuario: int
    fecha: str
    hora_inicio: str
    hora_fin: str
    personas: int
    estado: str


@app.get("/")
def root():
    return {"message": "Sistema de reservas de salas"}


@app.post("/reservas")
def crear_reserva(reserva: Reserva):
    for r in reservas:
        if r["id_reserva"] == reserva.id_reserva:
            raise HTTPException(status_code=400, detail="Ya existe una reserva con ese ID")
    
    reservas.append(reserva.model_dump())
    return {"message": "Reserva registrada exitosamente", "reserva": reserva}


@app.get("/reservas")
def obtener_reservas():
    return {"total": len(reservas), "reservas": reservas}