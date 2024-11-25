from clase import*
cola =[]
cuentas =[]
def crear_cuenta(cuentas):
    print("-Ingrese sus datos ")
    nombre = input("ingrese su nombre: ")
    cuenta = int(input("ingrese el numero de cuenta: "))
    saldo = float(input("ingrese la cantidad de saldo incial: "))
    usuario = Cuenta(nombre,cuenta,saldo)
    cuentas.append(usuario)

def consulta_saldo(cuentas):
    print("\n- Consultar Saldo ")
    cuenta_numero = int(input("Ingrese el número de su cuenta: "))
    for cuenta in cuentas:
        if cuenta.cuenta == cuenta_numero:
            print(f"Saldo actual: ${cuenta.saldo}")
            return
    print("Cuenta no encontrada.")

def deposito(cuentas):
    usuario = int(input("Ingrese el numero de cuenta: "))
    cuenta_encontrada = None
    for numero in cuentas:
        if numero.cuenta == usuario:
            cuenta_encontrada = numero
            break
    if cuenta_encontrada:
        try:
            cantidad = float(input("Ingrese la cantidad de dinero a depositar: "))
            if cantidad > 0:
                cuenta_encontrada.deposito(cantidad)
                print(f"Nuevo saldo de '{cuenta_encontrada.nombre}': {cuenta_encontrada.saldo}")
            else:
                print("La cantidad debe ser mayor que 0.")
        except ValueError:
            print("Error: ingrese un número válido.")
    else:
        print(f"El numero de cuenta: '{usuario}' no se encuentra en la base de datos.")

def retiro(cuentas):
    usuario = int(input("Ingrese el numero de cuenta: "))
    cuenta_encontrada = None
    for numero in cuentas:
        if numero.cuenta == usuario:
            cuenta_encontrada = numero
            break
    if cuenta_encontrada:
        try:
            cantidad = float(input("Ingrese la cantidad de dinero a retirar: "))
            if cantidad > 0:
                cuenta_encontrada.retiro_saldo(cantidad)
                print(f"Nuevo saldo de '{cuenta_encontrada.nombre}': {cuenta_encontrada.saldo}")
            else:
                print("Fondos insuficientes")
        except ValueError:
            print("Error: ingrese un número válido.")
    else:
        print(f"El numero de cuenta: '{usuario}' no se encuentra en la base de datos.")

def agregar_a_cola():
    print("\n agregar cliente a la cola ")
    nombre = input("Ingrese el nombre del cliente: ")
    numero_cuenta = int(input("Ingrese el número de cuenta del cliente: "))
    cliente = {"nombre": nombre, "numero_cuenta": numero_cuenta}
    cola.append(cliente)
    print(f"Cliente '{nombre}' agregado a la cola.")

def procesar_cola():
    print("\n- Procesar cliente de la cola ")
    if cola:
        cliente_actual = cola.pop(0)
        print(f"Atendiendo a: {cliente_actual['nombre']} (Cuenta: {cliente_actual['numero_cuenta']})")
        cuenta_encontrada = None
        for cuenta in cuentas:
            if cuenta.cuenta == cliente_actual["numero_cuenta"]:
                cuenta_encontrada = cuenta
                break
        if cuenta_encontrada:
            print("Seleccione una opcion:")
            print("1. Consultar saldo")
            print("2. Hacer un depósito")
            print("3. Retirar saldo")
            opcion = input("Opción: ")
            if opcion == "1":
                print(f"saldo actual: {cuenta_encontrada.saldo}")
            elif opcion == "2":
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                cuenta_encontrada.deposito(cantidad)
                print(f"deposito realizado. Nuevo saldo: {cuenta_encontrada.saldo}")
            elif opcion == "3":
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                cuenta_encontrada.retiro_saldo(cantidad)
                print(f"retiro realizado. nuevo saldo: {cuenta_encontrada.saldo}")
            else:
                print("opción no válida.")
        else:
            print(f"no se encontró una cuenta con el número {cliente_actual['numero_cuenta']}.")
    else:
        print("la cola está vacía.")

def mostrar_cola():
    print("\n- clientes en la cola ")
    if cola:
        for i, cliente in enumerate(cola, start=1):
            print(f"{i}. {cliente['nombre']} (Cuenta: {cliente['numero_cuenta']})")
    else:
        print("La cola está vacía.")

def gestionar_cola():
    while True:
        print("\n- gestión de Clientes en cola ")
        print("1. agregar cliente a la cola")
        print("2. procesar cliente")
        print("3. mostrar cola")
        print("4. regresar al menú principal")
        opcion = input("seleccione una opción: ")
        if opcion == "1":
            agregar_a_cola()
        elif opcion == "2":
            procesar_cola()
        elif opcion == "3":
            mostrar_cola()
        elif opcion == "4":
            break
        else:
            print("opcion no valida.")