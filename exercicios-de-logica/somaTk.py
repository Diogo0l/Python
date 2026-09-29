# Criação de um algoritmo utilizando a biblioteca Tkinter para criar uma interface gráfica que realiza a soma de dois números.

def somar():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor, insira números válidos.")

import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora de Soma")
janela.geometry("300x200")

# Cria os widgets
label1 = tk.Label(janela, text="Número 1:")
label1.pack(pady=5)

entry1 = tk.Entry(janela)
entry1.pack(pady=5)

label2 = tk.Label(janela, text="Número 2:")
label2.pack(pady=5)

entry2 = tk.Entry(janela)
entry2.pack(pady=5)

botao_somar = tk.Button(janela, text="Somar", command=somar)
botao_somar.pack(pady=10)

label_resultado = tk.Label(janela, text="Resultado: ")
label_resultado.pack(pady=5)

# Inicia o loop principal da janela
janela.mainloop()