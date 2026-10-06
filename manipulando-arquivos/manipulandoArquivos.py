try:
    with open('lista_de_compras.txt', 'r') as lista_de_compras:
        print(lista_de_compras.read())
except Exception as error:
    print(f'O arquivo não foi criado! {error}')