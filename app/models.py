import os
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from .db import Base

# Leemos el esquema asignado (ej: grupo_3)
SCHEMA = os.getenv("SCHEMA_NAME")

class Personal(Base):
    __tablename__ = "personal"
    # Definimos el schema aquí para que SQLAlchemy sepa dónde crear/leer la tabla
    __table_args__ = {"schema": SCHEMA} 

    idPersona = Column(Integer, primary_key=True, index=True) [cite: 131, 154]
    idCargo = Column(Integer)  # Referencia simple según la guía [cite: 132, 155]
    nombre = Column(String(50), nullable=False) [cite: 133, 156]
    documento = Column(String(50), unique=True) [cite: 134, 157]
    correo = Column(String(50)) [cite: 134, 158]
    telefono = Column(String(50)) [cite: 135, 159]
    estado = Column(Boolean, default=True) [cite: 136, 160]

class Formacion(Base):
    __tablename__ = "formacion"
    __table_args__ = {"schema": "grupo_3"}

    idFormacion = Column(Integer, primary_key=True, index=True) [cite: 138, 164]
    idPersona = Column(Integer, ForeignKey("grupo_3.personal.idPersona")) [cite: 139, 165, 172]
    nivelDeFormacion = Column(String(50)) [cite: 140, 166]
    tituloObtenido = Column(String(100)) [cite: 141, 166]
    institucion = Column(String(100)) [cite: 142, 167]
    fechaFinal = Column(Date) [cite: 143, 168]