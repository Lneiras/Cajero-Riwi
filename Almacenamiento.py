import json
import os

ARCHIVO_DATOS = "datos_cajero.json"

def cargar_datos():
    """Carga el saldo y movimientos desde el archivo JSON."""
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r") as archivo:
            return json.load(archivo)
    # Si no existe el archivo, inicia con saldo 0 y sin movimientos
    return {"saldo": 0, "movimientos": []}

def guardar_datos(datos):
    """Guarda el saldo y movimientos en el archivo JSON."""
    with open(ARCHIVO_DATOS, "w") as archivo:
        json.dump(datos, archivo, indent=4)


print(" ¡Bienvenido a tu Cajero de Confianza! ")