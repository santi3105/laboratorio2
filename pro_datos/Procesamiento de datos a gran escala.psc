Algoritmo sin_titulo
	Dimensionar matriz(100,3)
	Dimensionar usuarios(100)
	Dimensionar accesos(100)
	indice_matriz <- 1
	indice_usuarios <- 1
	definir resultado como logico
	Repetir
		Escribir 'Nombre de usuario o salir: '
		Leer nombre
		resultado = falso
		Si nombre='salir' Entonces
			Escribir "Usted esta saliendo del programa"
			resultado = verdadero
		SiNo
			Escribir 'Hora de entrada de ', nombre, ' (en fecha y hora): '
			Leer entrada
			Escribir 'Hora de salida de ', nombre, ' (en fecha y hora): '
			Leer salida
			matriz[indice_matriz,1]<-nombre
			matriz[indice_matriz,2]<-entrada
			matriz[indice_matriz,3]<-salida
			indice_matriz <- indice_matriz+1
		FinSi
	Hasta Que resultado==verdadero
	Para i<-1 Hasta indice_matriz Hacer
		usuario <- matriz[i,1]
		encontrado <- Falso
		Para j<-1 Hasta indice_usuarios Hacer
			Si usuarios[j]=usuario Entonces
				accesos[j] <- accesos[j]+1
				encontrado <- Verdadero
			FinSi
		FinPara
		Si  NO encontrado Entonces
			usuarios[indice_usuarios] <- usuario
			accesos[indice_usuarios] <- 1
			indice_usuarios <- indice_usuarios+1
		FinSi
	FinPara
	Para i<-1 Hasta indice_usuarios-1 Hacer
		Escribir 'Resultados de accesos por usuario:'
		Escribir 'Usuario: ', usuarios[i], ', Número de accesos: ', accesos[i]
	FinPara
FinAlgoritmo
