class Cuenta:
    def __init__(self,nombre,cuenta,saldo):
        self.nombre = nombre
        self.cuenta = cuenta
        self.saldo = saldo
    def deposito(self,cantidad):
        self.saldo += cantidad
    def retiro_saldo(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print(f"No hay suficiente saldo {self.nombre}.")