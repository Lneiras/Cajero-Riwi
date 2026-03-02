from Almacenamiento import guardar_datos

def consultarSaldo(datos):
    print("\n==================================")
    print("  Tu saldo actual es: $", datos["saldo"])
    print("==================================")

def depositarSaldo(datos):
    while True:
        monto = input("\nIngresa el valor que deseas depositar: $")

        if monto.isdigit() == False:
            print("Monto invalido, ingresa solo numeros enteros.")
            continue

        monto = int(monto)

        if monto <= 0:
            print("El monto debe ser mayor a cero. Intentalo de nuevo.")
            continue
        else:
            datos["saldo"] += monto
            datos["movimientos"].append({"tipo": "Deposito", "monto": monto})
            guardar_datos(datos)
            print("\nDeposito exitoso.")
            print("Tu nuevo saldo es: $", datos["saldo"])
            break

    return datos

def retirarSaldo(datos):
    while True:
        monto = input("\nIngresa el monto que deseas retirar: $")

        if monto.isdigit() == False:
            print("Monto invalido, ingresa solo numeros enteros.")
            continue

        monto = int(monto)

        if monto <= 0:
            print("El monto debe ser mayor a cero. Intentalo de nuevo.")
            continue
        elif monto > datos["saldo"]:
            print("Saldo insuficiente. Tu saldo actual es: $", datos["saldo"])
            continue
        else:
            datos["saldo"] -= monto
            datos["movimientos"].append({"tipo": "Retiro", "monto": monto})
            guardar_datos(datos)
            print("\nRetiro exitoso.")
            print("Tu nuevo saldo es: $", datos["saldo"])
            break

    return datos

def salir():
    print("\n==================================")
    print("  Gracias por usar el cajero.")
    print("  Ten un buen dia!")
    print("==================================")
