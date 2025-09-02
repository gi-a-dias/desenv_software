import tkinter as tk
from tkinter import *

# Função para tratar o clique no botão cadastrar
def cadastrar_funcionario():
    nome = entrada_nome.get().strip()
    cargo = cargo_selecionado.get()
    senha = entrada_senha.get()

    if not nome:
        messagebox.showwarning("Aviso", "Por favor, insira o nome.")
        return
    if not senha:
        messagebox.showwarning("Aviso", "Por favor, insira a senha.")
        return

    # Aqui você pode adicionar a lógica para salvar o funcionário
    messagebox.showinfo("Sucesso", f"Funcionário {nome} cadastrado como {cargo}.")

# Janela principal
janela = tk.Tk()
janela.title("Sistema de Gestão de Funcionários")
janela.geometry("400x300")
janela.resizable(True, True)

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