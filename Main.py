from Operaciones import consultarSaldo, DepositarSaldo, RetirarSaldo, Salir
from Almacenamiento import cargar_datos

def menu():
    """Menú principal del cajero."""
    print("\n" + "=" * 50)
    print("  CAJERO AUTOMÁTICO  ")
    print("=" * 50)
    print("  1. Consultar saldo",
          "  2. Depositar",
          "  3. Retirar",
          "  4. Salir",
            sep="\n")
    print("=" * 50)

def main(): 
    print(" ¡Bienvenido a tu Cajero de Confianza! ")

    datos = cargar_datos()

    while True:
        menu()
        opcion = int(input("¿Que operación desea realizar? : "))

        if opcion == 1:
            consultarSaldo(datos["saldo"])
        elif opcion == 2:
            datos = DepositarSaldo(datos)
        elif opcion == 3:
            datos = RetirarSaldo(datos)
        elif opcion == 4:
            Salir()
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main() 