from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Definimos la estructura del JSON que esperas
class Persona(BaseModel):
    nombre: str
    apellido: str
    edad: int

# Esta ruta recibe el JSON
@app.post("/persona")
def crear_persona(persona: Persona):
    # Aquí puedes procesar los datos
    return {
        "mensaje": "Datos recibidos correctamente",
        "datos_recibidos": persona,
        "saludo": f"Hola {persona.nombre}, bienvenido al servidor"
    }

# Esta ruta es para ver algo rápido en el navegador
@app.get("/")
def inicio():
    return {"status": "Servidor activo", "mensaje": "Usa /docs para probar el envío de JSON"}