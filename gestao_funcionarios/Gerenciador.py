import csv
from Administrativo import Administrativo
from Professor import Professor
from Tecnico import Tecnico


class GerenciadorFuncionarios:
    def __init__(self):
        self._funcionarios = []
        self.arquivo_csv = "funcionarios.csv"
        self.carregar_dados()

    def adicionar_funcionario(self, funcionario):
        for f in self._funcionarios:
            if f.cpf == funcionario.cpf:
                return False
        self._funcionarios.append(funcionario)
        self.salvar_dados()
        return True

    def listar_funcionarios(self):
        return self._funcionarios

    def salvar_dados(self):
        """Salva a lista de funcionários no arquivo CSV."""
        with open(self.arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
            escritor = csv.writer(file)
            escritor.writerow(['nome', 'cpf', 'salario_base', 'cargo', 'senha', 'atributo_especifico'])
            for func in self._funcionarios:
                atributo_especifico = ''
                if isinstance(func, Administrativo):
                    atributo_especifico = func.setor
                elif isinstance(func, Professor):
                    atributo_especifico = func.materia
                elif isinstance(func, Tecnico):
                    atributo_especifico = func.especializacao

                escritor.writerow([
                    func.nome, func.cpf, func.salario_base, func.cargo,
                    func._Funcionario__senha, atributo_especifico
                ])
        print(f"Dados salvos com sucesso em {self.arquivo_csv}")

    # A CORREÇÃO ESTÁ AQUI:
    # O 'def carregar_dados' foi movido para fora do 'salvar_dados' e agora
    # está alinhado com os outros métodos, pertencendo corretamente à classe.
    def carregar_dados(self):
        """Lê o arquivo CSV e preenche a lista de funcionários."""
        try:
            with open(self.arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
                leitor_csv = csv.reader(file)
                next(leitor_csv, None)
                self._funcionarios.clear()

                for linha in leitor_csv:
                    nome, cpf, salario_base_str, cargo, senha, atributo_especifico = linha
                    salario_base = float(salario_base_str)

                    novo_funcionario = None
                    if cargo == "Administrativo":
                        novo_funcionario = Administrativo(nome=nome, cpf=cpf, salario_base=salario_base, senha=senha,
                                                          setor=atributo_especifico)
                    elif cargo == "Professor":
                        novo_funcionario = Professor(nome=nome, cpf=cpf, salario_base=salario_base, senha=senha,
                                                     materia=atributo_especifico)
                    elif cargo == "Técnico":
                        novo_funcionario = Tecnico(nome=nome, cpf=cpf, salario_base=salario_base, senha=senha,
                                                   especializacao=atributo_especifico)

                    if novo_funcionario:
                        self._funcionarios.append(novo_funcionario)

            print(f"Dados carregados de '{self.arquivo_csv}' com sucesso.")
        except FileNotFoundError:
            print(f"Arquivo '{self.arquivo_csv}' não encontrado. Um novo será criado no primeiro cadastro.")
        except Exception as e:
            print(f"Ocorreu um erro ao carregar os dados: {e}")