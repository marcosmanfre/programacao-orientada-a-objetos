from abc import ABC, abstractmethod

class IFigura(ABC):

    @abstractmethod
    def CalculaArea(self):
        pass

    @abstractmethod
    def CalculaPerimetro(self):
        pass