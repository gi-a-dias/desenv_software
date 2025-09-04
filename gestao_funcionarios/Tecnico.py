from Funcionario import Funcionario
class Tecnico(Funcionario):
    def __init__(self, nome, cpf, salario_base, senha, especializacao):
        # Chamando a classe mãe, definindo o atributo cargo
        super().__init__(nome, cpf, salario_base, "Tecnico", senha)
        # atributo especial da classe-filha
        self.especializacao = especializacao
    def calcular_salario(self):
        salario_base_tec = super().calcular_salario()
        bonus_tec = salario_base_tec * 0.20
        salario_final = salario_base_tec + bonus_tec
        print(f"Salário para cargo técnico: R${salario_final:.2f}")
        return salario_final