class Cliente:
    def __init__(self, endereco:str):
        #privados
        self._endereco = endereco #somente string
        self._contas = [] #lista

    #metodos
    def realizar_transacao(self, conta, transacao):
        #chama o metodo registrar la de 'Transacao'
        transacao.registrar(conta)
        print("Transacao realizada com sucesso")

    def adicionar_conta(self, conta):
        #novo numero da conta na lista
        self._contas.append(conta)
        print(f"Conta {conta._numero} adicionada com sucesso")

