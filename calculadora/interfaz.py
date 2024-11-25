def menu():
    """
    muestra el menu de las figuras geometricas
    retor la variable opcion
    """
    print("\n Bienvenido a la calculadora de figuras")
    print("1)cuadrado")
    print("2)triangulo")
    print("3)circulo")
    print("4)rectangulo")
    print("5)rombo")
    print("6)romboide")
    print("7)trapecio")
    print("8)pentagono")
    print("9)salir")
    op = int(input("digite una opcion del menu: "))
    return op
def opcion_seleccionada(op):
    """
    mostrar la opcion seleccionada
    """
    if op == 1:
        print(f"usted selecciono la opcion cuadrado")
        return 1
    elif op == 2:
        print(f"usted selecciono la opcion triangulo")
        return 2
    elif op == 3:
        print(f"usted selecciono la opcion circulo")
        return 3
    elif op == 4:
        print(f"usted selecciono la opcion rectangulo")
        return 4
    elif op == 5:
        print(f"usted selecciono la opcion rombo")
        return 5
    elif op == 6:
        print(f"usted selecciono la opcion romboide")
        return 6
    elif op == 7:
        print(f"usted selecciono la opcion trapecio")
        return 7
    elif op == 8:
        print(f"usted selecciono la opcion pentagono")
        return 8
    elif op == 9:
        print(f"saliendo de la calculadora...")
        return 9
    else:
        return"opcin no valida!!!"
def datos_cuadrado():
    """
    solicita el lado para calculo de area
    lado, tipo de dato float
    """
    lado= float(input("digite el lado: "))
    return lado
def datos_circulo():
    """
    solicita el radio para calculo de area
    radio, tipo de dato float
    """
    radio= float(input("digite el radio: "))
    return radio
def datos_rectangulo ():
    """
    solicita la base y la altura para calculo de area
    ambos, tipo de dato float
    """
    base = float(input("ingrese la base: "))
    altura = float(input("digite la altura"))
    return base,altura
def datos_rombo():
    """
    solicita la Diagonal mayor y la diagonal menor para calculo de area
    ambos, tipo de dato float
    """
    D = float(input("ingrese la diagonal mayor: "))
    d = float(input("ingrese la diagonal menor: "))
    return D,d
def datos_trapecio():
    """
    solicita la Base mayor, la base menor y la altura para calculo de area
    los tres, tipo de dato float
    """
    B = float(input("ingrese la base mayor : "))
    b = float(input("ingrese la base menor: "))
    h = float(input("ingrese la altura: "))
    return B,b,h
def datos_pentagono():
    """
    solicita el perimetro y la apotema para calculo de area
    ambos, tipo de dato float
    """
    P = float(input("ingrese el perimetro: "))
    a = float(input("ingrese el apotema : "))
    return P,a