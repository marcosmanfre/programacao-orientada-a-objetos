from Funcionario import Funcionario
from Vendedor import Vendedor

vendedor1 = Vendedor("Stallone ", 55, 1800, 500)
print(vendedor1)


vendedor1.calculaSalario()
print("O Salario do Vendedor é: " + str(vendedor1.calculaSalario()))