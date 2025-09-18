from Cliente import Cliente
from datetime import date
class PessoaFisica(Cliente):
    def __init__(self, cpf:str, nome:str, data_nascimento:date, endereco:str):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    #getters
    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def data_nascimento(self):
        return self._data_nascimento
