from pathlib import Path

pasta_atual = Path(__file__).parent.absolute()

# Abrindo o arquivo lista_de_compras.txt para leitura
'''with open(pasta_atual / 'lista_de_compras.txt', 'r', encoding='utf-8') as lista_de_compras:
    print(lista_de_compras.read())'''
    
# Abrindo um arquivo linha por linha
with open(pasta_atual / 'lista_de_compras.txt', 'r', encoding='utf-8') as lista_de_compras:
    '''for linha in lista_de_compras:
        print(linha.strip())'''  # strip() remove espaços em branco no início e no final da linha
    linha = lista_de_compras.readline()
    while linha != '':
        print(linha, end='')  # end='' evita que o print adicione uma nova linha
