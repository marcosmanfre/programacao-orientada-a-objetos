class Funcionario:

# construtor
    def __init__(self, matricula, nome, dataAdmissao, valorHora, valorHoraExtra, cargo, status):
        self.__matricula = matricula
        self.__nome = nome
        self.__dataAdmissao = dataAdmissao
        self.__valorHora = valorHora
        self.__valorHoraExtra = valorHoraExtra
        self.__cargo = cargo
        self.__status = status


# metodos acessadores das propriedades
    def getMatricula(self):
        return self.__matricula
    
    def setMatricula(self, matricula):
        self.__matricula = matricula
    
    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getDataAdmissao(self):
        return self.__dataAdmissao
    
    def setDataAdmissao(self, dataAdmissao):
        self.__dataAdmissao = dataAdmissao

    def getValorHora(self):
        return self.__valorHora

    def setValorHora(self, valorHora):
        self.__valorHora = valorHora

    def getValorHoraExtra(self):
        return self.__valorHoraExtra

    def setValorHoraExtra(self, valorHoraExtra):
        self.__valorHoraExtra = valorHoraExtra

    def getCargo(self):
        return self.__cargo
    
    def setCargo(self, cargo):
        self.__cargo = cargo

    def getStatus(self):
        return self.__status
    
    def setStatus(self, status):
        self.__status = status,
    

#métodos
    def calcularSalario(self, qtdeHoras):
        return self.__valorHora * qtdeHoras
      
    def calcularHorasExtras(self, qtdeHorasExtras):
        return self.__valorHoraExtra * qtdeHorasExtras

    def reajustarValorHora(self, Reasjuste):
        return self.__valorHora  + (self.__valorHora * Reasjuste / 100),  self.__valorHoraExtra + (self.__valorHoraExtra * Reasjuste / 100)

    def __str__(self):
        return " Matricula : " + str(self.__matricula) + " Nome : " + self.__nome + " Data Admissão : " + str(self.__dataAdmissao) + " Valor Hora : " + str(self.__valorHora) + " Valor Hora Extra : " + str(self.__valorHoraExtra) + " Cargo: " + str(self.__cargo) + " Status: " + str(self.__status)   
