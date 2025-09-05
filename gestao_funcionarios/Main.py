import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk


from Funcionario import Funcionario
from Administrativo import Administrativo as ClasseAdmin
from Professor import Professor as ClasseProfessor
from Tecnico import Tecnico as ClasseTecnico
from Gerenciador import GerenciadorFuncionarios

gerenciador = GerenciadorFuncionarios()

def atualizar_campos_especificos(*args):
    cargo_escolhido = cargo_selecionado.get()
    # Esconde todos os campos específicos para começar do zero
    label_setor.grid_remove(); entrada_setor.grid_remove()
    label_materia.grid_remove(); entrada_materia.grid_remove()
    label_especializacao.grid_remove(); entrada_especializacao.grid_remove()

    if cargo_escolhido == "Administrativo":
        label_setor.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        entrada_setor.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
    elif cargo_escolhido == "Professor":
        label_materia.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        entrada_materia.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
    elif cargo_escolhido == "Técnico":
        label_especializacao.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        entrada_especializacao.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

def atualizar_tabela_funcionarios():
    for item in tabela_funcionarios.get_children():
        tabela_funcionarios.delete(item)
    for func in gerenciador.listar_funcionarios():
        salario_final = func.calcular_salario()
        tabela_funcionarios.insert("", tk.END, values=[func.nome, func.cargo, f"{salario_final:.2f}"])

def cadastrar_funcionario():
    nome = entrada_nome.get().strip()
    cpf = entrada_cpf.get().strip()
    salario_base_fixo = Funcionario.SALARIO_MINIMO
    cargo = cargo_selecionado.get()
    senha = entrada_senha.get().strip()

    if not all([nome, cpf, senha]):
        messagebox.showwarning("Aviso", "Nome, CPF e Senha são obrigatórios.")
        return

    novo_funcionario = None
    if cargo == "Administrativo":
        setor = entrada_setor.get().strip()
        if setor: novo_funcionario = ClasseAdmin(nome=nome, cpf=cpf, salario_base=salario_base_fixo, senha=senha, setor=setor)
    elif cargo == "Professor":
        materia = entrada_materia.get().strip()
        if materia: novo_funcionario = ClasseProfessor(nome=nome, cpf=cpf, salario_base=salario_base_fixo, senha=senha, materia=materia)
    elif cargo == "Técnico":
        especializacao = entrada_especializacao.get().strip()
        if especializacao: novo_funcionario = ClasseTecnico(nome=nome, cpf=cpf, salario_base=salario_base_fixo, senha=senha, especializacao=especializacao)

    if not novo_funcionario:
        messagebox.showwarning("Aviso", "O campo específico do cargo (Setor, Matéria, etc.) é obrigatório.")
        return

    sucesso = gerenciador.adicionar_funcionario(novo_funcionario)
    if sucesso:
        atualizar_tabela_funcionarios()
        messagebox.showinfo("Sucesso", f"Funcionário {novo_funcionario.nome} cadastrado!")
        # Limpeza
        entrada_nome.delete(0, tk.END); entrada_cpf.delete(0, tk.END); entrada_senha.delete(0, tk.END)
        entrada_setor.delete(0, tk.END); entrada_materia.delete(0, tk.END); entrada_especializacao.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", f"CPF {novo_funcionario.cpf} já cadastrado.")

#"Cara" da janela
janela = ttk.Window(themename="litera")
janela.title("Sistema de Gestão de Funcionários")

# Frame do Formulário
form_frame = ttk.Labelframe(janela, text="Dados do Funcionário")
form_frame.pack(fill="x", padx=20, pady=10)

# Nome
ttk.Label(form_frame, text="Nome:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entrada_nome = ttk.Entry(form_frame)
entrada_nome.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

# CPF
ttk.Label(form_frame, text="CPF:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
entrada_cpf = ttk.Entry(form_frame)
entrada_cpf.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

# Cargo (menu suspenso)
ttk.Label(form_frame, text="Cargo:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
opcoes_cargo = ["Administrativo", "Professor", "Técnico"]
cargo_selecionado = tk.StringVar(value=opcoes_cargo[0])
menu_cargo = ttk.OptionMenu(form_frame, cargo_selecionado, opcoes_cargo[0], *opcoes_cargo)
menu_cargo.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

# Campos Específicos (são criados aqui, mas aparecem e somem conforme a função)
label_setor = ttk.Label(form_frame, text="Setor:")
entrada_setor = ttk.Entry(form_frame)
label_materia = ttk.Label(form_frame, text="Matéria:")
entrada_materia = ttk.Entry(form_frame)
label_especializacao = ttk.Label(form_frame, text="Especialização:")
entrada_especializacao = ttk.Entry(form_frame)

# Senha
ttk.Label(form_frame, text="Senha:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
entrada_senha = ttk.Entry(form_frame, show="*")
entrada_senha.grid(row=4, column=1, sticky="ew", padx=5, pady=5)

# Botão Cadastrar
botao_cadastrar = ttk.Button(form_frame, text="Cadastrar", bootstyle="success")
botao_cadastrar.grid(row=5, column=0, columnspan=2, pady=15)

form_frame.columnconfigure(1, weight=1)

#Tabela de Visualização
tabela_frame = ttk.Labelframe(janela, text="Funcionários Cadastrados")
tabela_frame.pack(fill="both", expand=True, padx=20, pady=10)
colunas = ("nome", "cargo", "salario_final")
tabela_funcionarios = ttk.Treeview(tabela_frame, columns=colunas, show="headings")
tabela_funcionarios.heading("nome", text="Nome")
tabela_funcionarios.heading("cargo", text="Cargo")
tabela_funcionarios.heading("salario_final", text="Salário Final (R$)")
tabela_funcionarios.pack(fill="both", expand=True)

#Loop Principal e conexoes
# Conectamos os botões e eventos às funções DEPOIS que tudo foi criado
botao_cadastrar.config(command=cadastrar_funcionario)
cargo_selecionado.trace_add("write", atualizar_campos_especificos)

# definir o estado inicial da tela
atualizar_campos_especificos()
atualizar_tabela_funcionarios()

# Inicia o programa
janela.mainloop()