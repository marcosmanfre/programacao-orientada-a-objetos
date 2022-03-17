from Funcionario import Funcionario
from Assistente import Assistente

assistente1 = Assistente("Arnold ", 98, 2000)
print(assistente1)

assistente1.calculaSalario()
print("O Salario do Assistente é: " + str(assistente1.calculaSalario()))