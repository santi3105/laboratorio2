Algoritmo sin_titulo
		Dimensionar producto(100, 2)  
		Dimensionar cantidad[100]      
		productosRegistrados <- 0      
		Definir op, rta, agregar, vender Como Entero 
		
		Repetir
			Escribir 'Gesti�n de productos'
			Escribir '1. Ver cat�logo de productos'
			Escribir '2. Agregar stock a los productos'
			Escribir '3. Agregar un nuevo producto'
			Escribir '4. Realizar venta'
			Escribir '5. Salir'
			Escribir 'Seleccione una opci�n:'
			Leer op
			
			Si op == 1 Entonces
				Escribir 'Cat�logo de productos:'
				Para i <- 1 Hasta productosRegistrados Hacer
					Escribir 'Producto n�mero: ', i, ' | Nombre: ', producto[i, 1], ' | Precio: ', producto[i, 2], ' | Cantidad: ', cantidad[i]
				FinPara
				
			SiNo Si op == 2 Entonces
					Escribir "Seleccione el n�mero del producto al que desea agregar stock:"
					Leer rta
					Si rta >= 1 Y rta <= productosRegistrados Entonces
						Escribir "Ingrese la cantidad a agregar:"
						Leer agregar
						cantidad[rta] <- cantidad[rta] + agregar
						Escribir "Stock actualizado correctamente."
					SiNo
						Escribir "Opci�n inv�lida."
					FinSi
					
				SiNo Si op == 3 Entonces
						Si productosRegistrados < 100 Entonces
							productosRegistrados <- productosRegistrados + 1
							Escribir 'Ingrese el nombre del nuevo producto:'
							Leer producto[productosRegistrados, 1]
							Escribir 'Ingrese el precio unitario del producto:'
							Leer producto[productosRegistrados, 2]
							Escribir 'Ingrese la cantidad inicial del producto:'
							Leer cantidad[productosRegistrados]
							Escribir "Producto registrado correctamente."
						SiNo
							Escribir "No se pueden registrar m�s productos "
						FinSi
						
					SiNo Si op == 4 Entonces
							Escribir "Seleccione el n�mero del producto a vender:"
							Leer rta
							Si rta >= 1 Y rta <= productosRegistrados Entonces
								Escribir "Ingrese la cantidad a vender:"
								Leer vender
								Si vender <= cantidad[rta] Entonces
									cantidad[rta] <- cantidad[rta] - vender
									Escribir "Venta realizada correctamente"
								SiNo
									Escribir "Stock insuficiente para realizar la venta"
								FinSi
							SiNo
								Escribir "Opci�n no valida"
							FinSi
							
						SiNo Si op == 5 Entonces
								Escribir "Saliendo del sistema"
								
							SiNo
								Escribir "Opci�n no v�lida. Intente de nuevo."
							FinSi
						fin si
					fin si
				fin si 
			fin si 
		Hasta Que op == 5

FinAlgoritmo
