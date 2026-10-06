# Desafio
'''
Fase inicial: 
- [x] Crie uma lista com os itens e o valor para uma compra de um supermercado;
- [ ] Crie um loop para introduzir os itens na lista;
- [ ] Crie um menu com opção de parar ou continuar.
- [ ] Mostre a lista e o valor total da compra.
'''

# lista dos itens
lista_itens = ['abóbora', 'melancia', 'banana', 'manga']

while True:
    print("Menu:")
    print("1. Adicionar item")
    print("2. Parar")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        item = input("Digite o nome do item: ")
        valor = float(input("Digite o valor do item: "))
        lista_itens.append((item, valor))
    elif opcao == '2':
        break
    else:
        print("Opção inválida. Tente novamente.")