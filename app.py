import random
import string
import tkinter as tk
import tkinter.messagebox as messagebox
import pyperclip

def gerar_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def copiar_senha(senha):
    pyperclip.copy(senha)

def gerar_senha_gui():
    # Cria a janela
    janela = tk.Tk()
    janela.title("Gerador de Senhas")

    # Cria o campo de entrada para o tamanho da senha
    tamanho_label = tk.Label(janela, text="Tamanho da senha:")
    tamanho_label.grid(row=0, column=0, padx=5, pady=5)
    tamanho_entry = tk.Entry(janela)
    tamanho_entry.grid(row=0, column=1, padx=5, pady=5)

    # Cria o campo de saída para a senha gerada
    senha_label = tk.Label(janela, text="Senha gerada:")
    senha_label.grid(row=1, column=0, padx=5, pady=5)
    senha_output = tk.Label(janela, text="")
    senha_output.grid(row=1, column=1, padx=5, pady=5)

    # Cria o botão para gerar a senha
    def gerar():
        tamanho_str = tamanho_entry.get()
        if not tamanho_str.isdigit():
            messagebox.showerror("Erro", "Por favor, digite um número inteiro para o tamanho da senha.")
            return
        tamanho = int(tamanho_str)
        senha = gerar_senha(tamanho)
        senha_output.config(text=senha)

    gerar_button = tk.Button(janela, text="Gerar Senha", command=gerar)
    gerar_button.grid(row=2, column=1, padx=5, pady=5)

    # Cria o botão para copiar a senha para a área de transferência
    def copiar():
        senha = senha_output.cget("text")
        if not senha:
            messagebox.showerror("Erro", "Por favor, gere uma senha antes de copiá-la.")
            return
        copiar_senha(senha)
        messagebox.showinfo("Senha Copiada", "A senha foi copiada para a área de transferência.")

    copiar_button = tk.Button(janela, text="Copiar Senha", command=copiar)
    copiar_button.grid(row=2, column=0, padx=5, pady=5)

    janela.mainloop()

gerar_senha_gui()
