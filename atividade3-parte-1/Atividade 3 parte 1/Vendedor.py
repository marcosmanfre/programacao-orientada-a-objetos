from Funcionario import Funcionario

class Vendedor(Funcionario):

        def __init__(self, nome, matricula, salario_base, comissao):
            super().__init__(nome, matricula, salario_base)
            self.__comissao = comissao


        def getComissao(self):
            return self.__comissao

        def setComissao(self, comissao):
            self.__comissao = comissao
        
        def calculaSalario(self):
            return (super().getSalarioBase()) + (self.__comissao)


        def __str__(self):
            return super().__str__() + " Comissão: " + str(self.__comissao)