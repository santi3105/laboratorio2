Algoritmo sin_titulo
	Definir saldo, deposito, retiro Como Real
    saldo <- 0
    Definir totalClientes, clienteActual, cliente Como Entero
	
    // Leer la cantidad de clientes
    Escribir "Ingrese la cantidad de clientes:"
    Leer totalClientes
	
    // Dimensionar la cola de clientes según el número ingresado
    Dimensionar colaClientes[totalClientes]
	
    // Leer los números de los clientes
    Para i <- 1 Hasta totalClientes Con Paso 1
        Escribir "Ingrese el número del cliente ", i, ":"
        Leer colaClientes[i]
    FinPara
	
    clienteActual <- 1
	
    Mientras clienteActual <= totalClientes
        cliente <- colaClientes[clienteActual]
        Escribir "Atendiendo al cliente ", cliente
		
        // Solicitar monto a depositar
        Escribir "Ingrese el monto que desea depositar el cliente ", cliente, ":"
        Leer deposito
        saldo <- saldo + deposito
        Escribir "Cliente deposita ", deposito, ". Nuevo saldo: ", saldo
		
        // Solicitar monto a retirar
        Escribir "Ingrese el monto que desea retirar el cliente ", cliente, ":"
        Leer retiro
        Si retiro <= saldo Entonces
            saldo <- saldo - retiro
            Escribir "Cliente retira ", retiro, ". Nuevo saldo: ", saldo
        Sino
            Escribir "Error: Saldo insuficiente para retirar ", retiro
        FinSi
		
        Escribir "El saldo actual de la cuenta es: ", saldo
		
        clienteActual <- clienteActual + 1
    FinMientras
FinAlgoritmo
