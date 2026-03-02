from Almacenamiento import cargar_datos
from Operaciones import consultarSaldo, depositarSaldo, retirarSaldo, salir

def menu():
    print("\n" + "=" * 50)
    print("                CAJERO AUTOMÁTICO  ")
    print("=" * 50)
    print("  1. Consultar saldo",
          "  2. Depositar",
          "  3. Retirar",
          "  4. Salir",
            sep="\n")
    print("=" * 50)

def main():
    print("\n" + "=" * 50)
    print("       ¡Bienvenido a tu Cajero de Confianza!")
    

    datos = cargar_datos()

    while True:
        menu()
        opcion = input("¿Que operacion deseas realizar hoy?: ")

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
            print("opcion invalida, por favor intentalo de nuevo.")

main()
