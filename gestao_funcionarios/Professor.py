from Funcionario import Funcionario
class Professor(Funcionario):
    def __init__(self, nome, cpf, salario_base, senha, materia):
        # Chamando a classe mãe, definindo o atributo cargo
        super().__init__(nome, cpf, salario_base, "Professor", senha)
        # atributo especial da classe-filha
        self.materia = materia
    def calcular_salario(self):
        salario_base_prof = super().calcular_salario()
        bonus_prof = 1000
        salario_final = salario_base_prof + bonus_prof
        print(f"Salário para professor: R${salario_final:.2f}")
        return salario_final