matriz =[]
print("ingrese el nombre del usuario, para terminar escriba 'salir'")

while True:
    nombre=input("nombre de usuario o salir: ")
    if nombre == 'salir'  :
        break
    entrada = input(f"Hora de entrada de {nombre} en fecha y hora ")
    salida = input(f"Hora de salida de {nombre} en fecha y hora ")
    matriz.append({"usuario": nombre, "entrada": entrada, "salida": salida})

resultados = []
conteo_accesos = {}

i = 0
while i < len(matriz):
    registro = matriz[i]
    usuario = registro["usuario"]
    if usuario in conteo_accesos:
        conteo_accesos[usuario] += 1
    else:
        conteo_accesos[usuario] = 1
    i += 1

for usuario, accesos in conteo_accesos.items():
    resultados.append([usuario, accesos])
print("Resultados de accesos por usuario:")
for resultado in resultados:
    print(f"Usuario: {resultado[0]}, Número de accesos: {resultado[1]}")