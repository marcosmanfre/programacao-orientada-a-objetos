from datetime import date, datetime
from ContaBancaria import ContaBancaria



class ContaPoupanca(ContaBancaria):

 #construtor

    def __init__(self, nomeCliente, numConta, agencia, Saldo, DiadeRendimento, taxadeRendimento):
        super().__init__(nomeCliente, numConta, agencia, Saldo)
        self.__DiadeRendimento = DiadeRendimento
        self.__taxadeRendimento = taxadeRendimento


#métodos acessadores das propriedades

    def getDiadeRendimento(self):
        return self.__DiadeRendimento

    def setDiadeRendimento(self, DiadeRendimento):
        self.__DiadeRendimento = DiadeRendimento

    def getTaxadeRendimento(self):
        return self.__taxadeRendimento

    def setTaxadeRendimento(self, taxadeRendimento):
        self.__taxadeRendimento = taxadeRendimento


#métodos


    from datetime import datetime
 
    def calcularNovoSaldo(self, dia,):
        if (datetime.today().strftime('%Y-%m-%d') <= (dia)):
            self.__Saldo * self.__taxadeRendimento
       
    def __str__(self):
        return super().__str__() + " Dia Rendimento: " + str(self.__DiadeRendimento) + " Taxa Rendimento: " + str(self.__taxadeRendimento)