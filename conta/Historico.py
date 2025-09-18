class Historico:
    def __init__(self):
        self._transacoes = [] #lista para armazenar o historico

    def adicionar_transacao(self, transacao):
        #metodo usado em Deposito e Saque
        self._transacoes.append(transacao)
        print("Transacao adicionada ao historico.")