from pathlib import Path

pasta_atual = Path(__file__).parent.absolute()

# Abrindo o arquivo lista_de_compras.txt para leitura
'''with open(pasta_atual / 'lista_de_compras.txt', 'r', encoding='utf-8') as lista_de_compras:
    print(lista_de_compras.read())'''
    
# Abrindo um arquivo linha por linha
'''with open(pasta_atual / 'lista_de_compras.txt', 'r', encoding='utf-8') as lista_de_compras:
    for linha in lista_de_compras:
        print(linha.strip())'''  # strip() remove espaços em branco no início e no final da linha
        
'''lista_de_compras = open('lista_de_compras.txt', 'r', encoding='utf-8')
itens_lista_compra = lista_de_compras.readlines()
lista_atualizada = open('lista_de_compras_atualizada.txt', 'w', encoding='utf-8')

itens_ja_comprados = ['ovos', 'leite'] 

with open(pasta_atual / 'lista_de_compras.txt', 'r', encoding='utf-8') as lista_de_compras:
    itens_lista_compra = lista_de_compras.readlines()
    
with open('lista_de_compras.txt', 'r') as lista_de_compras:
    for item in itens_lista_compra:
        if item.strip() not in itens_ja_comprados:
            lista_atualizada.write(item)
            print(f'Item {item.strip()} adicionado à lista de compras atualizada.')'''
            
itens_a_adicionar = ['arroz', 'feijão', 'macarrão']

with open(pasta_atual / 'lista_de_compras.txt', 'a', encoding='utf-8') as lista_de_compras:
    for item in itens_a_adicionar:
        lista_de_compras.write(f'{item}\n')
        print(f'Item {item} adicionado à lista de compras.') 