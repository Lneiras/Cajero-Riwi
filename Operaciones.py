

def consultarSaldo(saldo):
    print("su saldo es: ", saldo)

def RetirarSaldo(saldo, Montoaretirar):
    while True:
        try:
            Montoaretirar = int(input("Ingresa el monto que deseas retirar: "))
        except ValueError:
            print("Entrada no válida, ingresa un número entero")
            continue

        if Montoaretirar <= 0:
            print("Has ingresado un monto errado, inténtalo de nuevo")
            continue
        elif Montoaretirar > saldo:
            print("Saldo insuficiente")
            continue

        saldo -= Montoaretirar
        print("Retiro exitoso")
        print("Tu nuevo saldo es:", saldo)
        return saldo


def DepositarSaldo(saldo, Monto_a_depositar):
    while True:
        try:
            Monto_a_depositar = int(input("Ingresa el valor que deseas depositar: "))
        except ValueError:
            print("Entrada no válida, ingresa un número entero")
            continue

        if Monto_a_depositar <= 0:
            print("Has ingresado un monto errado, intentalo de nuevo")
            continue

        else:
            saldo += Monto_a_depositar
            print("Deposito exitoso",
                "Tu nuevo saldo es: ", saldo,
                sep="\n")
        return saldo

def Salir():
    print("Gracias por utilizar nuestros servicios",
        "Ten un buen día",
        sep="\n")
        