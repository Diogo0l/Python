import random
import tkinter as tk


def gerar_palpite():
    numero = random.sample(range(1, 61), 5)
    resultado_label.config(text=f"Palpite da Mega-Sena: {', '.join(map(str, numero))}")

janela = tk.Tk()
janela.title("Palpite da Mega-Sena")
janela.config(bg="#f0f0f0")
janela.geometry("300x200")
janela.label = tk.Label(janela, text="Clique no botão para gerar um palpite da Mega-Sena:", font=("Arial", 12), fg="black", )

resultado_label = tk.Label(janela, text="Palpite da Mega-Sena: ")
resultado_label.pack(pady=20)
janela.button = tk.Button(janela, text="Gerar Palpite", command=gerar_palpite)
janela.button.pack(pady=1)

janela.mainloop()