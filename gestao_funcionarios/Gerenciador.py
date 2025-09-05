class GerenciadorFuncionarios:
    def __init__(self):
        self._funcionarios = []
        #Aprendizado novo: _f... diz que a lista é interna
    def adicionar_funcionario(self, funcionario):
        # Verificação de CPF duplicado
        for f in self._funcionarios:
            if f.cpf == funcionario.cpf:
                #Se o cpf ja existe
                return False

        # Se não encontrou CPF duplicado, adiciona à lista e retorna True
        self._funcionarios.append(funcionario)
        return True

    def listar_funcionarios(self):
        #retorna a lista completa
        return self._funcionarios