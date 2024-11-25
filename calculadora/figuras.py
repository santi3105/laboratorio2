import math
def area_cuadrado(lado):
    """
    calcula el area del cuadrado
    area = lado * lado, tipo float
    tipo float
    """ 
    return lado*lado
def area_triangulo(base,altura):
    """
    calcula el area del triangulo
    area = (base *altura)/2
    tipo float
    """
    return (base*altura)/2
def area_circulo (radio):
    """
    calcula el area del circulo
    area = pi*r**2
    tipo float
    """ 
    return math.pi*radio**2
def area_rectangulo(base,altura):
    """
    calcula el area del rectangulo
    area = (base *altura)
    tipo float
    """
    return base*altura
def area_rombo(D,d):
    """
    calcula el area del rombo
    area = (Diametro mayor * diametro menor)/2
    tipo float
    """
    return (D*d)/2
def area_trapecio(B,b,h):
    """
    calcula el area del trapecio
    area = ((Base mayor + base menor)/2)*h
    tipo float
    """
    return ((B+b)/2)*h
def area_pentagono(perimetro,apotema):
    """
    calcula el area del pentagono
    area = (perimetro * apotema)/2
    tipo float
    """
    return (perimetro*apotema)/2