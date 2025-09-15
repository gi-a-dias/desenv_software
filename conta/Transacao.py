#importar ABC, classe para interface
from abc import ABC, abstractmethod

from arrow.util import validate_ordinal


class Transacao(ABC):
    @abstractmethod #carimbo para tornar o metodo obrigatorio nas filhas
    def registrar(self, conta):
        #contrato da interface com as filhas
        pass

#Como o projeto é pequeno podemos deixar as classes filhas aqui
class Deposito(Transacao):
    #atributo privado e float
    def __init__(self, conta):
        self._valor = float(valor)

    #metodo obrigatorio
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self._valor) #acessa o metodo da classe conta
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
        print(f'Depósito de R$ {self._valor:.2f} realizado com sucesso.')

class Saque(Transacao):
    def __init__(self, conta):
        self._valor = float(valor)

    #metodo obrigaotrio
    def registrar(self, conta):
        sucesso_transacoa = conta.sacar(self._valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
        print(f'Saque de R${self._valor:.2f} realizado com sucesso.')