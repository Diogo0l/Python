from bicicletario import Bicicleta
from bottle import get, post, request, route, run


@route('/')
@get('/')
def index():
    color = request.query.get('opcao')

    form =  '''
            <h1>Escolha uma opção</h1>
                <a href="/cadastro">Adicionar bicicleta</a>
                <br>
                <a href="/mostrar">Mostrar informações da bicicleta</a>
                <br>
                <a href="/acoes">Ações da bicicleta</a>
                <br>
            '''
    page = f'''
                <h1>Web App</h1>
                <body style="background-color:{color};">
                {form}
                </body>
            '''
    return page


@route('/cadastro')
def cadastro_de_bicicleta():
    form =  '''
            <form action="/process" method="post">
                Qual a cor: <input type="text" name="cor">
                <br>
                Qual o modelo: <input type="text" name="modelo">
                <br>
                Qual o ano: <input type="text" name="ano">
                <br>
                Qual o valor: <input type="text" name="valor">
                <br>
                <input type="submit">
            </form>
            '''
    page = f'<h1>Web App</h1>{form}'
    return page


def carregar_bicicletas():
    """Lê o arquivo txt"""
    bicicletas = []
    with open('bicicletas.txt', 'r', encoding='utf-8') as file:
        for linha in file:
                    partes = linha.strip().split('|')
                    valor_float = float(partes[3])
                    bicicletas.append(Bicicleta(partes[0],partes[1],partes[2],valor_float))
    return bicicletas

def salvar_bicicleta(bicicletas):
    with open('bicicletas.txt', 'w', encoding='utf-8') as file:
        for bicicleta in bicicletas:
            linha = f'{bicicleta.cor}|{bicicleta.modelo}|{bicicleta.ano}|{bicicleta.valor}\n'
            file.write(linha)

@post('/process')
def index_process():    
    bicicletas = carregar_bicicletas()

    cor = request.forms.get('cor')
    modelo = request.forms.get('modelo')
    ano = request.forms.get('ano')
    valor = request.forms.get('valor')
    bicicletas.append(Bicicleta(cor, modelo, ano, valor))
    
    # Salvar em um arquivo txt, ou em um banco de dados sqlite
    salvar_bicicleta(bicicletas)
    message = f'A bicicleta {modelo} {cor}, de {ano} com valor {valor} foi adicionada!'

    return message

@route('/mostrar')
def mostrar_bicicletas():
    bicicletas = carregar_bicicletas()

    page =  '''
                <h1>Listagem de Bicicletas </h1>
                <ul>                
                '''
    for bicicleta in bicicletas:
         page += f'<li>Cor: {bicicleta.cor}, Modelo: {bicicleta.modelo}, Ano: {bicicleta.ano}, Valor: {bicicleta.valor}'

    page += '</ul>'
    return page

run(host='localhost', port=8080)