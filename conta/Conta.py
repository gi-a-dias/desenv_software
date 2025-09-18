from Cliente import Cliente
from Historico import Historico

class Conta():
    #Atributos (todos privados)
    def __init__(self, numero:int, cliente: Cliente):
        self._saldo = 0.0 #float
        self._numero = numero
        self._agencia = "0001" #string
        self._Cliente = cliente
        self._Historico = Historico()

    #metodos
    @property
    def saldo(self):
        return self._saldo

    @property
    def historico(self):
        return self._Historico

    @property
    def cliente(self):
        return self._Cliente
    def sacar(self, valor: float):
        if valor>0 and self._saldo >= valor:
            self._saldo -= valor
            print(f'Saque de R$ {valor:.2f} realizado. Novo saldo de R$ {self._saldo:.2f}')
            return True
        else:
            print(f"Tentativa de saque de R$ {valor:.2f} falhou. Saldo insuficiente")
            return False

    def depositar(self, valor: float) -> bool:
        def depositar(self, valor: float) -> bool:
            if valor > 0:
                self._saldo += valor
                print(f"Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self._saldo:.2f}")
                return True
            else:
                print("Valor de depósito inválido.")
                return False