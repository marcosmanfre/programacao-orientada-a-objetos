from datetime import datetime
from ContaPoupanca import ContaPoupanca
from ContaBancaria import ContaBancaria

conta2 = ContaPoupanca("Alfredo", 558898, 10, 1000, "2021-09-19", 10)
print(conta2)



conta2.calcularNovoSaldo("2021-09-19")