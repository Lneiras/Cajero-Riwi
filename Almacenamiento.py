import json
import os

ARCHIVO_DATOS = "datos_cajero.json"

def cargar_datos():
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r") as archivo:
            return json.load(archivo)
    return {"saldo": 0, "movimientos": []}

def guardar_datos(datos):
    with open(ARCHIVO_DATOS, "w") as archivo:
        json.dump(datos, archivo, indent=4)
