class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def aumentar_stock(self, cantidad):
        self.cantidad += cantidad

    def disminuir_stock(self, cantidad):
        if cantidad > self.cantidad:
            print(f"No hay suficiente stock de {self.nombre}.")
        else:
            self.cantidad -= cantidad


class Factura:
    def __init__(self):
        self.items = []
        self.subtotal = 0

    def agregar_item(self, producto, cantidad):
        if cantidad > producto.cantidad:
            print(f"No hay suficiente stock de {producto.nombre}.")
            return
        subtotal_producto = producto.precio * cantidad
        self.items.append({"producto": producto, "cantidad": cantidad, "subtotal": subtotal_producto})
        self.subtotal += subtotal_producto
        producto.disminuir_stock(cantidad)

    def mostrar_factura(self):
        print("\n- Detalle de Factura ")
        for item in self.items:
            p = item["producto"]
            print(f"{p.nombre} x {item['cantidad']} - Subtotal: ${item['subtotal']}")
        print(f"total: ${self.subtotal}")

