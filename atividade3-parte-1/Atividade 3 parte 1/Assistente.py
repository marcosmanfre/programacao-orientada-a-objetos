from Funcionario import Funcionario

class Assistente(Funcionario):
        
        def calculaSalario(self):
            return super().getSalarioBase()