from clase import *

catalogo = []

def agregar_producto(catalogo):
    try:
        print("Agregar producto")
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad de unidades del producto: "))
        producto = Producto(nombre, precio, cantidad)
        catalogo.append(producto)
        print(f"Producto '{nombre}' agregado correctamente.")
    except ValueError:
        print("Error: valor no válido.")

def lista_de_productos(catalogo):
    if not catalogo:
        print("\nEl catálogo está vacío.")
    else:
        print("\n- Catálogo de Productos ")
        for p in catalogo:
            print(f" Nombre: {p.nombre}, Precio: ${p.precio}, Cantidad disponible: {p.cantidad}")

def agregar_stock(catalogo):
    objeto = input("Ingrese el nombre del producto: ")
    producto_encontrado = None
    for producto in catalogo:
        if producto.nombre == objeto:
            producto_encontrado = producto
            break
    if producto_encontrado:
        try:
            cantidad = int(input("Ingrese la cantidad de stock a añadir: "))
            if cantidad > 0:
                producto_encontrado.aumentar_stock(cantidad)
                print(f"Nuevo stock de '{producto_encontrado.nombre}': {producto_encontrado.cantidad}")
            else:
                print("La cantidad debe ser mayor que 0.")
        except ValueError:
            print("Error: ingrese un número válido.")
    else:
        print(f"El producto '{objeto}' no se encuentra en el catálogo.")

def realizar_venta(catalogo):
    factura = Factura()
    while True:
        objeto = input("Ingrese el nombre del producto que desea comprar (o 'salir' para terminar): ")
        if objeto == 'salir':
            break
        producto_encontrado = None
        for producto in catalogo:
            if producto.nombre == objeto:
                producto_encontrado = producto
                break
        if producto_encontrado:
            try:
                cantidad = int(input(f"Ingrese la cantidad de {producto_encontrado.nombre} que desea comprar: "))
                if cantidad > 0:
                    factura.agregar_item(producto_encontrado, cantidad)
                else:
                    print("La cantidad debe ser mayor que 0.")
            except ValueError:
                print("Error: ingrese un número válido.")
        else:
            print(f"El producto '{objeto}' no se encuentra en el catálogo.")
    factura.mostrar_factura()
