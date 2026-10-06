# Desafio
"""
Fase inicial:
- [x] Crie uma lista com os itens e o valor para uma compra de um supermercado;
- [x] Crie um loop para introduzir os itens na lista;
- [x] Crie um menu com opção de parar ou continuar.
- [x] Mostre a lista e o valor total da compra.

Fase estruturada:
- [x] Organize os código em funções.
- [x] Crie uma função para salvar a lista e o total em um arquivo txt.
- [x] Crie uma nova opção no menu para salvar a lista.
"""

# lista dos itens
lista_itens = []
total = 0


def mostrar_menu():
    print("====== Menu: ======")
    print("1. Adicionar item")
    print("2. Mostrar itens e valor total")
    print("3. Salvar lista")
    print("4. Parar")
    opcao = input("Escolha uma opção: ")
    return opcao


def adicionar_item():
    item = input("Digite o nome do item: ")
    valor = float(input("Digite o valor do item: "))
    lista_itens.append((item, valor))
    return valor


def mostrar_itens():
    print("====== Itens na lista: ======")
    for item in lista_itens:
        print(f"{item}")
    print(f"Valor total da compra: R${total:.2f}")


def salvar_lista(): # O arquivo .txt deve ser salvo no mesmo diretório do desafio.py
    with open("lista_compra_desafio.txt", "w") as arquivo:
        arquivo.write("====== Itens na lista: ======\n")
        for item in lista_itens:
            arquivo.write(f"{item}\n")
        arquivo.write(f"Valor total da compra: R${total:.2f}\n")
    print("Lista salva no arquivo 'lista_compra_desafio.txt'.")

while True:
    opcao = mostrar_menu()
    if opcao == "1":
        total += adicionar_item()
    elif opcao == "2":
        mostrar_itens()
    elif opcao == "3":
        salvar_lista()
    elif opcao == "4":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")