from Almacenamiento import cargar_datos
from Operaciones import consultarSaldo, depositarSaldo, retirarSaldo, salir

def menu():
    print("\n==================================")
    print("      CAJERO AUTOMATICO")
    print("==================================")
    print("  1. Consultar saldo")
    print("  2. Depositar")
    print("  3. Retirar")
    print("  4. Salir")
    print("==================================")

def main():
    print("\nBienvenido a tu Cajero de Confianza!")

    datos = cargar_datos()

    while True:
        menu()
        opcion = input("Que operacion deseas realizar?: ")

        if opcion == "1":
            consultarSaldo(datos)
        elif opcion == "2":
            datos = depositarSaldo(datos)
        elif opcion == "3":
            datos = retirarSaldo(datos)
        elif opcion == "4":
            salir()
            break
        else:
            print("Opcion no valida. Elige entre 1 y 4.")

main()
