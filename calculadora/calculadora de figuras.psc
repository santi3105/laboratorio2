Algoritmo sin_titulo
	Definir op, lado, base, altura, diagonalMayor, diagonalMenor, radio, apotema, perimetro, area, bs_my, bs_mn Como Real
	Escribir 'Calculadora de �reas de Figuras Geom�tricas'
	Escribir 'Seleccione una figura:'
	Escribir '1. Cuadrado'
	Escribir '2. Rect�ngulo'
	Escribir '3. Rombo'
	Escribir '4. Romboide'
	Escribir '5. Trapecio'
	Escribir '6. Pent�gono'
	Escribir '7. C�rculo'
	Escribir '8. Tri�ngulo'
	Escribir '9. Salir'
	Leer op
	Si op==1 Entonces
		Escribir 'Ingrese el lado del cuadrado'
		Leer lado
		area <- lado*lado
		Escribir 'el area del cuadrado es', area
	SiNo
		Si op==2 Entonces
			Escribir 'Ingrese la base del rectangulo:'
			Leer base
			Escribir 'Ingrese la altura del rectangulo:'
			Leer altura
			area <- (base*altura)/2
			Escribir 'el area del rectangulo es: ', area
		SiNo
			Si op==3 Entonces
				Escribir 'Ingrese la diagonal mayor del rombo:'
				Leer diagonalMayor
				Escribir 'Ingrese la diagonal menor del rombo:'
				Leer diagonalMenor
				area <- (diagonalMayor*diagonalMenor)/2
				Escribir 'El �rea del rombo es: ', area
				
			SiNo
				Si op==4 Entonces
					Escribir 'Ingrese la base del romboide:'
					Leer base
					Escribir 'Ingrese la altura del romboide:'
					Leer altura
					area <- base*altura
					Escribir 'El �rea del romboide es: ', area
				SiNo
					Si op==5 Entonces
						Escribir 'Ingrese la base mayor del trapecio:'
						Leer bs_my
						Escribir 'Ingrese la base menor del trapecio:'
						Leer bs_mn
						Escribir 'Ingrese la altura del trapecio:'
						Leer altura
						area <- ((baseMayor+baseMenor)*altura)/2
						Escribir 'El �rea del trapecio es: ', area
					SiNo
						Si op==6 Entonces
							Escribir 'Ingrese el per�metro del pent�gono:'
							Leer perimetro
							Escribir 'Ingrese el apotema del pent�gono:'
							Leer apotema
							area <- (perimetro*apotema)/2
							Escribir 'El �rea del pent�gono es: ', area
						SiNo
							Si op==7 Entonces
								Escribir 'Ingrese el radio del c�rculo:'
								Leer radio
								area <- (3.1416*(radio/2))
								Escribir 'El �rea del c�rculo es: ', area
							SiNo
								Si op==8 Entonces
									Escribir 'Ingrese la base del rect�ngulo:'
									Leer base
									Escribir 'Ingrese la altura del rect�ngulo:'
									Leer altura
									area <- base*altura
									Escribir 'el area del rectangulo es: ', area
								SiNo
									Si op==9 Entonces
										Escribir "Saliendo del programa"
									SiNo
										Escribir "Opcion no valida"
									FinSi
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
