from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os
# 1. Creamos la aplicación del servidor
app = FastAPI(title="API El Chuzo de Bastian")
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

@app.post("/pedido")
def crear_pedido(pedido: Pedido):
    if os.path.exists("pedidos.json"):
        with open("pedidos.json", "r", encoding="utf-8") as f:
            try:
                listado_pedidos = json.load(f)
            except json.JSONDecodeError:
                listado_pedidos = []
    else:
        listado_pedidos = []

    listado_pedidos.append(pedido.dict())

    with open("pedidos.json", "w", encoding="utf-8") as f:
        json.dump(listado_pedidos, f, indent=4)

    return {"mensaje": "Pedido recibido con éxito", "datos": pedido.dict()}

