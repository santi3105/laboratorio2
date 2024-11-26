import random

filas = int(input("Ingresa el numero de zonas: "))
columnas = int(input("Ingresa el número de sensores por zona: "))
temperatura_min= int(input("ingrese la temperatura minima de los sensores: "))
temperatura_max= int(input("ingrese la temperatura maxima de los sensores: "))
temperatura_critica= int(input("ingrese la temperatura critica: "))

temperaturas=[]
for i in range(filas):
    fila = []
    for j in range(columnas):
            valor= random.randint(temperatura_min,temperatura_max)
            fila.append(valor)
    temperaturas.append(fila)
    for fila in temperaturas:
        print(fila)

def detectar_temperaturas_criticas(temperaturas, temperatura_critica):
    posiciones_criticas = []
    for i in range(len(temperaturas)):
        for j in range(len(temperaturas[i])):
            if temperaturas[i][j] > temperatura_critica:
                posiciones_criticas.append((i, j, temperaturas[i][j]))
    return posiciones_criticas

valores= detectar_temperaturas_criticas(temperaturas,temperatura_critica)

for fila, columnas,temperatura in valores:
    print(f"Sensor en ({fila}, {columnas}) = {temperatura}°C")
