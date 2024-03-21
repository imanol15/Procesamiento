# main.py
from fastapi import FastAPI, HTTPException
from models import Concentrador, DatosGenerador
from typing import List

app = FastAPI()
concentrador = Concentrador()

@app.post("/generador/", status_code=201)
async def recibir_datos_produccion(datos: DatosGenerador):
    if concentrador.validar_datos(datos):
        # Aquí se podrían procesar o guardar los datos recibidos
        print(f"Datos recibidos del generador {datos.id}: {datos}")
        return {"status": "Datos recibidos y validados"}
    else:
        raise HTTPException(status_code=400, detail="Datos inválidos")


@app.get("/agregados/")
async def obtener_datos_agregados():
    datos_agregados = concentrador.agregar_datos()
    return datos_agregados

@app.get("/datos-generadores/", response_model=List[DatosGenerador])
async def leer_datos_generadores():
    # Esta función devolvería los últimos datos generados por cada generador
    datos_generadores = concentrador.obtener_datos_generadores()
    return datos_generadores
