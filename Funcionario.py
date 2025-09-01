class Funcionario:
    def __init__(self, nome, idade, salario_base, cargo, senha):
        self.nome = nome
        self.idade = idade
        self.salario_base = salario_base
        self.cargo = cargo
        self.__senha = senha

    