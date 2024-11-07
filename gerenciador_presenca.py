import tkinter as tk
from tkinter import messagebox

# Dados iniciais
todos_alunos = {"Ana", "Carlos", "Pedro", "Maria", "João"}
alunos_presentes = set()

# Função para adicionar aluno como presente
def marcar_presenca():
    aluno = entrada_aluno.get()
    if aluno in todos_alunos:
        alunos_presentes.add(aluno)
        messagebox.showinfo("Presença", f"Presença de {aluno} registrada!")
    else:
        messagebox.showerror("Erro", f"Aluno {aluno} não está na lista.")
    atualizar_status()

# Função para exibir o status de todos os alunos
def atualizar_status():
    alunos_ausentes = todos_alunos - alunos_presentes
    status_texto = "Status de Presença dos Alunos:\n\n"
    for aluno in todos_alunos:
        status_texto += f"{aluno}: {'Presente' if aluno in alunos_presentes else 'Ausente'}\n"
    status_texto += f"\nAlunos Presentes: {alunos_presentes}\n"
    status_texto += f"Alunos Ausentes: {alunos_ausentes}\n"
    status_label.config(text=status_texto)

# Interface gráfica
janela = tk.Tk()
janela.title("Gerenciador de Presença dos Alunos")

# Entrada de texto e botão
entrada_aluno = tk.Entry(janela)
entrada_aluno.pack(pady=5)

botao_marcar = tk.Button(janela, text="Marcar Presença", command=marcar_presenca)
botao_marcar.pack(pady=5)

# Label para exibir o status
status_label = tk.Label(janela, text="", justify="left", font=("Helvetica", 12))
status_label.pack(pady=10)

# Inicializa o status de presença
atualizar_status()

# Inicia a aplicação
janela.mainloop()
