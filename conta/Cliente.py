class Cliente:
    def __init__(self, endereco:str, contas):
        #privados
        self._endereco = endereco #somente string
        self._contas = [] #lista

    #metodos
    def realizar_transacao(self, conta, transacao):
        #saque ou deposito, numero da contaa
    def adicionar_conta(self, conta):
        #novo numero da conta na lista
        self._contas.append(conta)

