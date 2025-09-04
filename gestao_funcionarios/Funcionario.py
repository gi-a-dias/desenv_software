class Funcionario:
    # Este valor é o mesmo para TODOS os funcionários.
    SALARIO_MINIMO = 1500.00

    def __init__(self, nome, cpf, salario_base, cargo, senha):
        self.nome = nome
        self.cpf = cpf
        # Garante que o salário base nunca seja menor que o piso
        self.salario_base = max(salario_base, Funcionario.SALARIO_MINIMO)
        self.cargo = cargo
        self.__senha = senha

    # METODO CORRIGIDO
    def calcular_salario(self):
        # O comportamento correto do "pai" é simplesmente retornar o salário BASE.
        # As classes filhas usarão este valor como ponto de partida.
        return self.salario_base