from abc import ABC, abstractmethod

class Funcionario(ABC):

    def __init__(self, nome, matricula, salario_base):
        self.__nome = nome
        self.__matricula = matricula
        self.__salario_base = salario_base

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def getSalarioBase(self):
        return self.__salario_base

    def setSalarioBase(self, salario_base):
        self.__salario_base = salario_base

    @abstractmethod
    def calculaSalario(self):
        pass

    def __str__(self):
        return " Nome: " + self.__nome + " Matricula: " + str(self.__matricula) + " Salario Base: " + str(self.__salario_base)