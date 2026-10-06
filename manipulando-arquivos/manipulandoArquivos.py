from pathlib import Path

pasta_atual = Path(__file__).parent.absolute()
with open(pasta_atual / 'lista_de_compras.txt', 'r', encoding='utf-8') as lista_de_compras:
    print(lista_de_compras.read())

