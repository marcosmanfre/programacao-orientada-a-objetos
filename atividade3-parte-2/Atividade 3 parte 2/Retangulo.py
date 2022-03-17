from IFigura import IFigura

class Retangulo(IFigura):

    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def getBase(self):
        return self.__base
    
    def setBase(self, base):
        self.__base = base

    def getAltura(self):
        return self.__altura

    def setAltura(self, altura):
        self.__altura = altura


    def CalculaArea(self):
        return (self.__altura) * (self.__base)

    def CalculaPerimetro(self):
        return ((self.__base) * 2) + ((self.__altura) * 2)
