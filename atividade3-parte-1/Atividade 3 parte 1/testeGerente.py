from Funcionario import Funcionario
from Gerente import Gerente

gerente1 = Gerente("Batutinha ", 55, 2000)
print(gerente1)

gerente1.calculaSalario()
print("O Salario do Gerente é: " + str(gerente1.calculaSalario()))