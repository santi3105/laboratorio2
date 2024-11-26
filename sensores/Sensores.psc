Algoritmo sin_titulo
	definir n, m, i, j como entero
	definir criticos como cadena
	criticos = ''
	Escribir "Ingrese numero de filas"
	Leer n
	Escribir "Ingrese numero de columnas"
	Leer m
	Para i<-0 Hasta n-1 Hacer
		Para j<-0 Hasta m-1 Hacer
			Escribir "Ingrese el valor de sensor de la posicion (',i,',',j,'):"
		FinPara
	FinPara
	Escribir "Matriz generada"
	Para i<-0 Hasta n-1 Hacer
		Escribir "["
		Para j<-0 Hasta m-1 Hacer
			Si j<m-1 Entonces
				Escribir ','
			FinSi
		FinPara
		Escribir "]"
	FinPara
	Para i<-0 Hasta n-1 Hacer
		Para j<-0 Hasta m-1 Hacer
		
		FinPara
	FinPara
	Si criticos = '' Entonces
		Escribir "No se detectaron valores criticos"
	SiNo
		Escribir "Valores criticos detectados:"
		Escribir criticos
	FinSi
FinAlgoritmo
