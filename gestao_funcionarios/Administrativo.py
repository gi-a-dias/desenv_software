from Funcionario import Funcionario

class Administrativo(Funcionario):
    def __init__(self, nome, cpf, salario_base, senha, setor):
        # Chamando a classe mãe, definindo o atributo cargo
        super().__init__(nome, cpf, salario_base, "Administrativo", senha)
        # atributo especial da classe-filha
        self.setor = setor
    def calcular_salario(self):
        salario_base_adm = super().calcular_salario()
        bonus_adm = 300
        salario_final = salario_base_adm + bonus_adm
        print(f"Salário para cargo administrativo: R${salario_final:.2f}")
        return salario_final