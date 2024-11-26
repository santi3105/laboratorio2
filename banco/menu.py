from funciones import *
def menu():
    while True:
        print("\n- Gestión de Productos ")
        print("1. crear una cuenta")
        print("2. consulta de saldo")
        print("3. hacer un deposito")
        print("4. Retirar saldo")
        print("5. Gestion de clientes en cola")
        print("6. salir")
        opcion = input("seleccione una opción: ")

        if opcion == "1":
            crear_cuenta(cuentas)
        elif opcion == "2":
            consulta_saldo(cuentas)
        elif opcion == "3":
            deposito(cuentas)
        elif opcion == "4":
            retiro(cuentas)
        elif opcion == "5":
            gestionar_cola()
        elif opcion == "6":
            print("Gracias por usar el banco")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()