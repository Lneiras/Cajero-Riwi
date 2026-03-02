# Cajero Automático

`_Simulación de un cajero automático desarrollado en Python. Permite consultar saldo, depositar y retirar dinero, guardando los movimientos entre sesiones._`

---

## Estructura del proyecto

```
Cajero-Riwi/
- Main.py              # Punto de entrada, menú principal
- Operaciones.py       # Funciones de cada operación
- Almacenamiento.py    # Lectura y escritura del archivo JSON
- datos_cajero.json    # Generado automáticamente al ejecutar
- README.md
```

---

##  Funcionalidades

| Opción | Descripción |
|--------|-------------|
| 1. Consultar saldo | Muestra el saldo disponible |
| 2. Depositar | Agrega dinero a la cuenta |
| 3. Retirar | Descuenta dinero con validación de saldo |
| 4. Salir | Cierra el programa |

> El saldo y los movimientos se guardan en `datos_cajero.json`, por lo que se conservan aunque el programa se cierre.

---

## Cómo ejecutar

1. Clona el repositorio:
```bash
git clone https://github.com/Lneiras/Cajero-Riwi.git
```

2. Entra a la carpeta:
```bash
cd Cajero-Riwi
```

3. Ejecuta el programa:
```bash
python Main.py
```

---

##  Ramas del repositorio

| Rama | Uso |
|------|-----|
| `main` | Código estable en producción |
| `dev` | Desarrollo de nuevas funciones |
| `qa` | Pruebas antes de pasar a main |





