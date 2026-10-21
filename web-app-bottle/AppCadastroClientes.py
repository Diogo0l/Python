import sqlite3

from bottle import get, post, redirect, request, run, template

DB_NAME = "web-app-bottle/cadastroClientes.db" # Banco de dados


@get("/")
def index():
    msg_erro = request.query.get("erro", "")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email, telefone FROM clientes;")
    clientes = cursor.fetchall()
    conn.close()

    # Chama o arquivo views/indexCadastroClientes.tpl enviando os parâmetros
    return template("web-app-bottle/views/indexCadastroClientes", lista_clientes=clientes, msg_erro=msg_erro)


@get("/cadastrar")
def exibir_formulario_cadastro():
    return template("web-app-bottle/views/cadastrarCliente")


@post("/cadastrar")
def cadastrar_cliente():
    nome = request.forms.get("nome")
    email = request.forms.get("email")
    telefone = request.forms.get("telefone")

    # Valida os campos
    if not nome or not email:
        redirect("/?erro=Preencha+todos+os+campos")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?);",
        (nome, email, telefone)
    )

    conn.commit()
    conn.close()

    # Volta para a página inicial após cadastrar
    redirect("/")


@get("/editar/<id:int>")
def exibir_formulario_edicao(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email, telefone FROM clientes WHERE id = ?;", (id,))
    cliente = cursor.fetchone()
    conn.close()

    if not cliente:
        redirect("/?erro=Cliente+não+encontrado")

    # Chama o arquivo views/editarCadastroClientes.tpl
    return template("web-app-bottle/views/editarCadastroClientes", cliente=cliente)


@post("/editar/<id:int>")
def salvar_edicao(id):
    nome = request.forms.get("nome")
    email = request.forms.get("email")
    telefone = request.forms.get("telefone")

    if not nome or not email:
        redirect("/?erro=Preencha+todos+os+campos")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Atualiza o registro do cliente específico no banco de dados
    cursor.execute(
        "UPDATE clientes SET nome = ?, email = ?, telefone = ? WHERE id = ?;",
        (nome, email, telefone, id)
    )
    
    conn.commit()
    conn.close()

    # Redireciona de volta para a lista principal após salvar
    redirect("/")


@get("/deletar/<id:int>")
def deletar_cliente(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM clientes WHERE id = ?;",
        (id,)
    )

    conn.commit()
    conn.close()

    redirect("/")


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True, reloader=True)
