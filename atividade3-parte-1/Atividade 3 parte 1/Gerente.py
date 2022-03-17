from Funcionario import Funcionario

class Gerente(Funcionario):
        
        def calculaSalario(self):
            return super().getSalarioBase() * 2
    