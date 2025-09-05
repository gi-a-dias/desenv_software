import tkinter as tk
#from tkinter import *
from tkinter import messagebox
from Administrativo import Administrativo as ClasseAdmin
from Professor import Professor as ClasseProfessor
from Tecnico import Tecnico as ClasseTecnico

def atualizar_campos_especificos(*args):
    # 1. Pega o cargo selecionado no menu
    cargo_escolhido = cargo_selecionado.get()

    # 2. Esconde TODOS os campos específicos para começar do zero
    label_setor.grid_remove()
    entrada_setor.grid_remove()
    label_materia.grid_remove()
    entrada_materia.grid_remove()
    label_especializacao.grid_remove()
    entrada_especializacao.grid_remove()

    # 3. Mostra APENAS o campo correto com base na escolha
    if cargo_escolhido == "Administrativo":
        label_setor.grid(row=4, column=0, sticky="w", pady=5)
        entrada_setor.grid(row=4, column=1, pady=5, sticky="ew")
    elif cargo_escolhido == "Professor":
        label_materia.grid(row=4, column=0, sticky="w", pady=5)
        entrada_materia.grid(row=4, column=1, pady=5, sticky="ew")
    elif cargo_escolhido == "Técnico":
        label_especializacao.grid(row=4, column=0, sticky="w", pady=5)
        entrada_especializacao.grid(row=4, column=1, pady=5, sticky="ew")


# Função para tratar o clique no botão cadastrar
def cadastrar_funcionario():
    # 1º e 2º PASSOS (Coleta e Validação) continuam os mesmos...
    nome = entrada_nome.get().strip()
    cargo = cargo_selecionado.get()
    senha = entrada_senha.get()

    if not nome or not senha:
        messagebox.showwarning("Aviso", "Por favor, insira o nome e a senha.")
        return

    # 3º PASSO: Lógica de criação e AGORA O CÁLCULO DO SALÁRIO
    novo_funcionario = None

    if cargo == "Administrativo":
        # Usamos dados fixos só para o exemplo funcionar sem novos campos
        novo_funcionario = ClasseAdmin(nome=nome, cpf="111.111.111-11", salario_base=2000, senha=senha,
                                       setor="Financeiro")

    elif cargo == "Professor":
        novo_funcionario = ClasseProfessor(nome=nome, cpf="222.222.222-22", salario_base=2000, senha=senha,
                                           materia="Python")

    elif cargo == "Técnico":
        novo_funcionario = ClasseTecnico(nome=nome, cpf="333.333.333-33", salario_base=2000, senha=senha,
                                         especializacao="Redes")

    # 4º PASSO: Se um funcionário foi criado, calculamos e mostramos o salário
    if novo_funcionario:
        # A MÁGICA ACONTECE AQUI!
        salario_final = novo_funcionario.calcular_salario()

        # Criamos uma mensagem de sucesso mais completa
        mensagem_sucesso = f"""
        Funcionário Cadastrado!
        ----------------------------------
        Nome: {novo_funcionario.nome}
        Cargo: {novo_funcionario.cargo}
        Salário Final Calculado: R$ {salario_final:.2f}
        """
        messagebox.showinfo("Sucesso", mensagem_sucesso)

        # Limpamos os campos para o próximo cadastro
        entrada_nome.delete(0, tk.END)
        entrada_senha.delete(0, tk.END)

# Importa a biblioteca ttkbootstrap e dá a ela o apelido de 'ttk'
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Janela principal agora usando ttkbootstrap com o tema "litera"
janela = ttk.Window(themename="litera")
janela.title("Sistema de Gestão de Funcionários")


# Frame central
frame = tk.Frame(janela)
frame.pack(expand=True, padx=20, pady=20)

# Nome
label_nome = tk.Label(frame, text="Nome:")
label_nome.grid(row=0, column=0, sticky="e", pady=5)
entrada_nome = tk.Entry(frame)
entrada_nome.grid(row=0, column=1, pady=5)

#CPF - faltou na primeira entrega
label_cpf = ttk.Label(frame, text="CPF:")
label_cpf.grid(row=1, column=0, sticky="w", pady=5)
entrada_cpf = ttk.Entry(frame)
entrada_cpf.grid(row=1, column=1, pady=5, sticky="ew")

# Cargo (menu suspenso)
label_cargo = tk.Label(frame, text="Cargo:")
label_cargo.grid(row=2, column=0, sticky="e", pady=5) # <- atualização
opcoes_cargo = ["Administrativo", "Professor", "Técnico"]
cargo_selecionado = tk.StringVar()
cargo_selecionado.set(opcoes_cargo[0])
menu_cargo = tk.OptionMenu(frame, cargo_selecionado, *opcoes_cargo)
menu_cargo.grid(row=2, column=1, pady=5, sticky="we") # <- atualização

# Continuando a implementação do polimorfismo
#label e Entry criados, mas ainda nao na tela
# Campo para Administrativo
label_setor = ttk.Label(frame, text="Setor:")
entrada_setor = ttk.Entry(frame)

# Campo para Professor
label_materia = ttk.Label(frame, text="Matéria:")
entrada_materia = ttk.Entry(frame)

# Campo para Técnico
label_especializacao = ttk.Label(frame, text="Especialização:")
entrada_especializacao = ttk.Entry(frame)


# Senha
label_senha = ttk.Label(frame, text="Senha:")
label_senha.grid(row=5, column=0, sticky="w", pady=5) # row era 4, agora é 5
entrada_senha = ttk.Entry(frame, show="*")
entrada_senha.grid(row=5, column=1, pady=5, sticky="ew") # row era 4, agora é 5


# Botão Cadastrar
botao_cadastrar = ttk.Button(frame, text="Cadastrar", command=cadastrar_funcionario, bootstyle="success-outline")
botao_cadastrar.grid(row=6, column=0, columnspan=2, pady=15) # row era 5, agora é 6

# Bloco de codigo para o menu funcionar em tempo real
# 1. A linha abaixo diz: "sempre que o valor de cargo_selecionado mudar,
# execute a função atualizar_campos_especificos".
cargo_selecionado.trace_add("write", atualizar_campos_especificos)

# 2. Chamamos a função uma vez no início para definir o estado inicial da tela.
atualizar_campos_especificos()

# Ajustar colunas para expandir
frame.columnconfigure(1, weight=1)

# Exibir a janela
janela.mainloop()