from interfaz import*
from figuras import *
while True:
    try:
        op = menu()
        figuras = opcion_seleccionada(op)
        if figuras == 1:
            lado =  datos_cuadrado()
            area =area_cuadrado(lado)
            print(f"el area del cuadrado es: {area}")
        elif figuras == 2:
            base,altura =datos_rectangulo()
            area= area_triangulo(base,altura)
            print(f"el area del triangulo es: {area}")
        elif figuras == 3:
            radio =datos_circulo()
            area = area_circulo(radio)
            print(f"el area del circulo es: {area}")
        elif figuras == 4:
            base,altura =datos_rectangulo()
            area = area_rectangulo(base,altura)
            print(f"el area del rectangulo es: {area}")
        elif figuras == 5:
            D,d =datos_rombo()
            area = area_rombo(D,d)
            print(f"el area del rombo es: {area}")
        elif figuras == 6:
            base,altura =datos_rectangulo()
            area = area_rectangulo(base, altura)
            print(f"el area del romboide es: {area}")
        elif figuras == 7:
            B,b,h =datos_trapecio()
            area = area_trapecio(B,b,h)
            print(f"el area del trapecio es: {area}")
        elif figuras == 8:
            P,a =datos_pentagono()
            area = area_pentagono(P,a)
            print(f"el area del pentagono es: {area}")
        elif figuras == 9:
            break
        else:
            print("opcion no valida")
    except ValueError:
        print("ingrese una opcion")
print("gracias por usar la calculadora")