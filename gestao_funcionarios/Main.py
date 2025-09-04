import tkinter as tk
#from tkinter import *
from tkinter import messagebox
from Administrativo import Administrativo as ClasseAdmin
from Professor import Professor as ClasseProfessor
from Tecnico import Tecnico as ClasseTecnico

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

# Cargo (menu suspenso)
label_cargo = tk.Label(frame, text="Cargo:")
label_cargo.grid(row=1, column=0, sticky="e", pady=5)
opcoes_cargo = ["Administrativo", "Professor", "Técnico"]
cargo_selecionado = tk.StringVar()
cargo_selecionado.set(opcoes_cargo[0])
menu_cargo = tk.OptionMenu(frame, cargo_selecionado, *opcoes_cargo)
menu_cargo.grid(row=1, column=1, pady=5, sticky="we")

# Senha
label_senha = tk.Label(frame, text="Senha:")
label_senha.grid(row=2, column=0, sticky="e", pady=5)
entrada_senha = tk.Entry(frame, show="*")
entrada_senha.grid(row=2, column=1, pady=5)

# Botão Cadastrar
botao_cadastrar = tk.Button(frame, text="Cadastrar", command=cadastrar_funcionario)
botao_cadastrar.grid(row=3, column=0, columnspan=2, pady=15)

# Ajustar colunas para expandir
frame.columnconfigure(1, weight=1)

# Exibir a janela
janela.mainloop()