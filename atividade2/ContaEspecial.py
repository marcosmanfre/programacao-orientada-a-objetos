from ContaBancaria import ContaBancaria


class ContaEspecial(ContaBancaria):

#construtor

    def __init__(self, nomeCliente, numConta, agencia, Saldo, ValorLimite):
        super().__init__(nomeCliente, numConta, agencia, Saldo)
        self.__ValorLimite = ValorLimite



#métodos acessadores das propriedades

    def getValorLimite(self):
        return self.__ValorLimite

    def setValorLimite(self, ValorLimite):
        self.__ValorLimite = ValorLimite


#métodos

    def sacar(self, valor):
         return super().sacar(valor)
#não consegui redefinir esse método


    def __str__(self):
        return super().__str__() + " Valor Limite: " + str(self.__ValorLimite)