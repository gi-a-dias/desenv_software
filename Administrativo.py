import Funcionario
class Administrativo(Funcionario):
    def __init__(self, nome, senha, setor):
        super().__init__(nome, senha)
        self.setor = setor