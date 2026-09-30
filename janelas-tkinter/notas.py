"""
Crie um app que mostre no console a média de 3 notas.
Usando o Exemplo de Listar Notas, crie um app com janelas em Python para receber 3 notas e mostrar a média na janela.

Algoritmo:
- [x] Calcular a média das notas
- [x] Mostrar a média no console
- [x] Criar as funções
- [ ] Criar a janela
"""

import tkinter as tk


def receber_nota_console():
    nota = float(input("Digite a nota: "))
    if nota < 0 or nota > 10:
        print("Nota inválida. Digite uma nota entre 0 e 10.")
        return receber_nota_console()
    return nota


def mostrar_media_console(media):
    nota1 = receber_nota_console()
    nota2 = receber_nota_console()
    nota3 = receber_nota_console()
    media = calcular_media(nota1, nota2, nota3)
    print(f"A média das notas é: {media:.2f}")


# Função para calcular a média
def calcular_media(nota1, nota2, nota3):

    media = (nota1 + nota2 + nota3) / 3
    return media


def janela_media():
    """Mostra a média das notas em uma janela. usando Tkinter"""


janela = tk.Tk()
janela.configure(bg="lightgray")
janela.title("Média das Notas")
janela.label = tk.Label(
    janela, text="Média das Notas", font=("Arial", 24), bg="lightblue"
)  # Cria um label com o texto "Olá, Mundo!"
janela.geometry("400x300")
label = tk.Label(janela, text="Digite as 3 notas:", bg="lightgray", font=("Arial", 14))
label.pack(pady=10)
entry_nota1 = tk.Entry(janela, font=("Arial", 12))
entry_nota1.pack(pady=5)
entry_nota2 = tk.Entry(janela, font=("Arial", 12))
entry_nota2.pack(pady=5)
entry_nota3 = tk.Entry(janela, font=("Arial", 12))
entry_nota3.pack(pady=5)
label_resultado = tk.Label(janela, text="", bg="lightgray", font=("Arial", 14))
label_resultado.pack(pady=10)

def receber_notas_janela():
    nota1 = float(entry_nota1.get())
    nota2 = float(entry_nota2.get())
    nota3 = float(entry_nota3.get())
    media = calcular_media(nota1, nota2, nota3)
    label_resultado.config(text=f"A média das notas é: {media:.2f}")
    
janela.button_calcular = tk.Button(
    janela, text="Calcular Média", command=receber_notas_janela, font=("Arial", 12)
)
janela.button_calcular.pack(pady=10)


janela.mainloop()
