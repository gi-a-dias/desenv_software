#importar ABC, classe para interface
from abc import ABC, abstractmethod
from Conta import Conta

class Transacao(ABC):
    @abstractmethod #carimbo para tornar o metodo obrigatorio nas filhas
    def registrar(self, conta):
        #contrato da interface com as filhas
        pass

#Como o projeto é pequeno podemos deixar as classes filhas aqui
#Classe Filha: Deposito
class Deposito(Transacao):
    #atributo privado e float
    def __init__(self, valor):
        self._valor = float(valor)

    def registrar(self, conta: Conta):
        if conta.depositar(self._valor):
            conta.historico.adicionar_transacao(self)
            print("Transação de depósito registrada no histórico.")

#Classe filha: Saque
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = float(valor)

    #metodo obrigaotrio
    def registrar(self, conta: Conta):
        if conta.sacar(self._valor):
            conta.historico.adicionar_transacao(self)
            print("Transação de saque registrada no histórico.")