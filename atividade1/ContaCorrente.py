class ContaCorrente:

#construtor
    def __init__(self, nome, CPF, banco, agencia, contaCorrente, saldo, limite):
        self.__nome = nome
        self.__CPF = CPF
        self.__banco = banco
        self.__agencia = agencia
        self.__contaCorrente = contaCorrente
        self.__saldo = saldo
        self.__limite = limite


# metodos acessadores das propriedades
    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome
    
    def getCPF(self):
        return self.__CPF
    
    def setCPF(self, CPF):
        self.__CPF = CPF

    def getAgencia(self):
        return self.__agencia

    def setAgencia(self, agencia):
        self.__agencia = agencia

    def getContaCorrente(self):
        return self.__contaCorrente

    def setContaCorrente(self, contaCorrente):
        self.__contaCorrente = contaCorrente
        
    def getSaldo(self):
        return self.__saldo

    def setSaldo(self, saldo):
        self.__saldo = saldo

    def getLimite(self):
        return self.__limite

    def setLimite(self,limite):
        self.__limite = limite


#metodos
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__nome))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor



    def __str__(self):
        return "Nome: " + self.__nome + " CPF: " + self.__CPF + " Banco: " + self.__banco + " Agencia: " + self.__agencia + " Conta Corrente: " + self.__contaCorrente + " Saldo: " + str(self.__saldo) + " Limite: " + str(self.__limite)