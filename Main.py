import tkinter as tk

# Janela principal
janela = tk.Tk()
janela.title("Sistema de Gestão de Funcionários")
janela.geometry("400x300")
janela.resizable(True, True)  # permite redimensionar horizontal e verticalmente

# Frame central
frame = tk.Frame(janela)
frame.pack(expand=True)

# Nome
label_nome = tk.Label(frame, text="Nome:")
label_nome.pack(pady=5)
entrada_nome = tk.Entry(frame)
entrada_nome.pack(pady=5)

# Cargo (menu suspenso)
label_cargo = tk.Label(frame, text="Cargo:")
label_cargo.pack(pady=5)
opcoes_cargo = ["Administrativo", "Professor", "Técnico"]
cargo_selecionado = tk.StringVar()
cargo_selecionado.set(opcoes_cargo[0])
menu_cargo = tk.OptionMenu(frame, cargo_selecionado, *opcoes_cargo)
menu_cargo.pack(pady=5)

# Senha
label_senha = tk.Label(frame, text="Senha:")
label_senha.pack(pady=5)
entrada_senha = tk.Entry(frame, show="*")
entrada_senha.pack(pady=5)

# Exibir a janela
janela.mainloop()