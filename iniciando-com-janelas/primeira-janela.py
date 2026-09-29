import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title("Minha Primeira Janela")
janela.configure(bg="lightblue")  # Define a cor de fundo da janela
janela.geometry("400x300")  # Define o tamanho da janela (largura x altura)
janela.label = tk.Label(janela, text="Olá, Mundo!", font=("Arial", 24), bg="lightblue")  # Cria um label com o texto "Olá, Mundo!" e define a fonte e a cor de fundo
janela.button = tk.Button(janela, text="Clique Aqui", font=("Arial", 16), command=lambda: print("Botão clicado!"))  # Cria um botão que imprime uma mensagem no console quando clicado
janela.input = tk.Entry(janela, font=("Arial", 16))  # Cria um campo de entrada de texto
janela.label.pack(pady=20)  # Adiciona o label à janela com um espa
janela.button.pack(pady=10)  # Adiciona o botão à janela com um espaçamento
janela.input.pack(pady=10)  # Adiciona o campo de entrada à janela com um espaçamento
janela.resizable(False, False)  # Impede que a janela seja redimensionada
janela.mainloop()