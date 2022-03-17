class ContaBancaria:


#construtor
    def __init__(self, nomeCliente, numConta, agencia, Saldo):
        self.__nomeCliente = nomeCliente
        self.__numConta = numConta
        self.__agencia = agencia
        self.__Saldo = Saldo



#métodos acessadores das propriedades

    def getNomeCliente(self):
        return self.__nomeCliente

    def setNomeCliente(self, nomeCliente):
        self.__nomeCliente = nomeCliente

    def getNumConta(self):
        return self.__numConta

    def setNumConta(self, numConta):
        self.__numConta = numConta

    def getAgencia(self):
        return self.__agencia
    
    def setAgencia(self, agencia):
        self.__agencia = agencia
    
    def getSaldo(self):
        return self.__Saldo

    def setSaldo(self, Saldo):
        self.__Saldo = Saldo


#métodos

    def sacar(self, valor):
        if(valor <= (self.__Saldo)):
            self.__Saldo -= valor
        else:
            print("O Valor {} passou do saldo".format(valor))

    def depositar(self, valor):
        self.__Saldo += valor
    
    def __str__(self):
        return " Nome Cliente: " + self.__nomeCliente + " Número Conta: " + str(self.__numConta) + " Agência: " + str(self.__agencia) + " Saldo: " + str(self.__Saldo) 


