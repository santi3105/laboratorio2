from funciones import *

def menu():
    while True:
        print("\n- gestion de Productos ")
        print("1. ver catálogo de productos")
        print("2. agregar stock a productos")
        print("3. agregar un nuevo producto")
        print("4. realizar una venta")
        print("5. salir")
        opcion = input("seleccione una opción: ")

        if opcion == "1":
            lista_de_productos(catalogo)
        elif opcion == "2":
            agregar_stock(catalogo)
        elif opcion == "3":
            agregar_producto(catalogo)
        elif opcion == "4":
            realizar_venta(catalogo)
        elif opcion == "5":
            print("gracias por usar el sistema.")
            break
        else:
            print("opción no valida. Intente nuevamente.")

if __name__ == "__main__":
    menu()

