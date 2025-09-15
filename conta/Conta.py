class Conta():
    #Atributos (todos privados)
    def __init__(self, saldo, numero, agencia, Cliente, Historico):
        self._saldo = float(saldo)
        self._numero = int(numero)
        self._agencia = str(agencia)
        #Cliente
        #Historico
    #metodos

    def retorna_saldo(self):
        return self._saldo
