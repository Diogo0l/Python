import sqlite3
from bottle import get, post, request, redirect, template, run

DB_NAME = "meu_banco_de_dados.db"


@get("/")
def index():
    msg_erro = request.query.get("erro", "")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM clientes;")
    clientes = cursor.fetchall()
    conn.close()

    # Chama o arquivo views/index.tpl enviando os parâmetros
    return template("web-app-bottle/views/indexCadastroClientes", lista_clientes=clientes, msg_erro=msg_erro)


@get("/editar/<id:int>")
def exibir_formulario_edicao(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM clientes WHERE id = ?;", (id,))
    cliente = cursor.fetchone()
    conn.close()

    if not cliente:
        redirect("/?erro=Cliente+não+encontrado")

    # Chama o arquivo views/editar.tpl
    return template("web-app-bottle/views/editarCadastroClientes", cliente=cliente)


# (Demais rotas de cadastrar, salvar_edicao e deletar mantêm a lógica do banco de dados)

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True, reloader=True)
