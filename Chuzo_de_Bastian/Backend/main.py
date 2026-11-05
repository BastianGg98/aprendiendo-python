from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os

# 1. Creamos la aplicación del servidor
app = FastAPI(title="API El Chuzo de Bastian")

# Ruta segura al archivo pedidos.json (funciona desde cualquier carpeta donde se prenda el servidor)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_PEDIDOS = os.path.join(BASE_DIR, "pedidos.json")

# 2. Permitimos que el HTML y JS se puedan conectar sin bloqueos (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. El molde (class) para validar los pedidos que llegan
class Pedido(BaseModel):
    cliente: str
    producto: str
    precio: float
    cantidad: int
    total: float = 0.0

@app.post("/pedido")
def crear_pedido(pedido: Pedido):
    if os.path.exists(ARCHIVO_PEDIDOS):
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as f:
            try:
                listado_pedidos = json.load(f)
            except json.JSONDecodeError:
                listado_pedidos = []
    else:
        listado_pedidos = []

    datos = pedido.dict()
    # Si no viene el total o viene en 0, lo calculamos acá
    if not datos.get("total"):
        datos["total"] = datos["precio"] * datos["cantidad"]

    listado_pedidos.append(datos)

    with open(ARCHIVO_PEDIDOS, "w", encoding="utf-8") as f:
        json.dump(listado_pedidos, f, indent=4)

    return {"mensaje": "Pedido recibido con éxito", "datos": datos}


@app.get("/pedidos")
def listar_pedidos():
    if os.path.exists(ARCHIVO_PEDIDOS):
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as f:
            try:
                listado_pedidos = json.load(f)
            except json.JSONDecodeError:
                listado_pedidos = []
    else:
        listado_pedidos = []

    return {"pedidos": listado_pedidos}