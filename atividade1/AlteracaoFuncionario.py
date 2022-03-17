from Funcionario import Funcionario

Funcionario1 = Funcionario(1, "Marcos", "21/05/2021", 20, 50, "Padeiro", "Ativo")
print(Funcionario1)

Funcionario2 = Funcionario(2, "Arnaldo", "22/03/2019", 40, 80, "Analista de Dados", "Ativo")
print(Funcionario2)

Funcionario1.setNome('Baltazar')
print(Funcionario1.getNome())
print(Funcionario1)

print("Salario: " + str(Funcionario1.calcularSalario(100)))

print("O valor de hora extra é: " + str(Funcionario1.calcularHorasExtras(30)))

print("O novo valor de horas normais e horas extras são: " + str(Funcionario1.reajustarValorHora(10)))

print("O novo valor de horas normais e horas extras são: " + str(Funcionario2.reajustarValorHora(10)))

