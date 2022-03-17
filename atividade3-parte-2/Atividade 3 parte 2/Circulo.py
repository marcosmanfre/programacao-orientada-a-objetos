import math
from IFigura import IFigura
from math import pi 

class Circulo(IFigura):
    pass

    def __init__(self, raio):
        self.__raio = raio

    def getRaio(self):
        return self.__raio

    def setRaio(self, raio):
        self.__raio = raio
    
    def CalculaArea(self):
        return math.pi * self.__raio ** 2

    def CalculaPerimetro(self):
        return 2 * math.pi * self.__raio