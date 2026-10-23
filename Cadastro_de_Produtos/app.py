import sqlite3
from pathlib import Path

from bottle import get, post, redirect, request, run, template

DB_PATH = Path(__file__).with_name("meu_banco_de_dados.db")
 
def get_connection():
    """Abre a conexão com o banco de dados configurada para acesso por nome de coluna."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
 
def inicializar_banco():
    """Cria as tabelas 'clientes' e 'produtos' no banco SQLite."""
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Tabela de Clientes
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        ''')
        
        # Tabela de Produtos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                preco REAL NOT NULL CHECK(preco >= 0.0),
                estoque INTEGER NOT NULL DEFAULT 0 CHECK(estoque >= 0)
            );
        ''')
        
        conn.commit()
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        print(f"Erro ao inicializar o banco de dados: {e}")
    finally:
        if conn:
            conn.close()
 
# ==========================================
# ROTAS DE CLIENTES
# ==========================================
 
@get('/')
def listar_clientes():
    msg_erro = request.query.get('erro', '')
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM clientes ORDER BY id DESC;")
    clientes = cursor.fetchall()
    conn.close()
    return template('cadastro_de_Produtos/views/clientes', lista_clientes=clientes, msg_erro=msg_erro)
 
@post('/cadastrar')
def cadastrar_cliente():
    nome = (request.forms.getunicode('nome') or '').strip()
    email = (request.forms.getunicode('email') or '').strip()
 
    if not nome or not email:
        redirect('/?erro=Preencha+todos+os+campos')
 
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", (nome, email))
        conn.commit()
        redirect('/')
    except sqlite3.IntegrityError:
        conn.rollback()
        redirect('/?erro=O+e-mail+já+está+cadastrado.')
    finally:
        conn.close()
 
@get('/editar/<id:int>')
def exibir_edicao_cliente(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email FROM clientes WHERE id = ?;", (id,))
    cliente = cursor.fetchone()
    conn.close()
 
    if not cliente:
        redirect('/?erro=Cliente+não+encontrado.')
 
    return template('Cadastro_de_Produtos/views/editarCLientes', cliente=cliente)
 
@post('/editar/<id:int>')
def salvar_edicao_cliente(id):
    nome = (request.forms.getunicode('nome') or '').strip()
    email = (request.forms.getunicode('email') or '').strip()
 
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?;", (nome, email, id))
        conn.commit()
        redirect('/')
    except sqlite3.IntegrityError:
        conn.rollback()
        redirect('/?erro=O+e-mail+pertence+a+outro+cliente.')
    finally:
        conn.close()
 
@get('/deletar/<id:int>')
def deletar_cliente(id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = ?;", (id,))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()
    finally:
        conn.close()
    redirect('/')
 
# ==========================================
# ROTAS DE PRODUTOS (NOVO MÓDULO)
# ==========================================
 
@get('/produtos')
def listar_produtos():
    msg_erro = request.query.get('erro', '')
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, preco, estoque FROM produtos ORDER BY id DESC;")
    produtos = cursor.fetchall()
    conn.close()
    return template('produtos', lista_produtos=produtos, msg_erro=msg_erro)
 
@post('/produtos/cadastrar')
def cadastrar_produto():
    nome = (request.forms.getunicode('nome') or '').strip()
    
    try:
        preco = float(request.forms.get('preco', 0))
        estoque = int(request.forms.get('estoque', 0))
    except ValueError:
        redirect('/produtos?erro=Preço+ou+estoque+inválidos.')
 
    if not nome or preco < 0 or estoque < 0:
        redirect('/produtos?erro=Informe+dados+válidos+para+o+produto.')
 
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?);", (nome, preco, estoque))
        conn.commit()
        redirect('/produtos')
    except sqlite3.Error as e:
        conn.rollback()
        redirect(f'/produtos?erro=Erro+ao+cadastrar+produto:+{e}')
    finally:
        conn.close()
 
@get('/produtos/editar/<id:int>')
def exibir_edicao_produto(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, preco, estoque FROM produtos WHERE id = ?;", (id,))
    produto = cursor.fetchone()
    conn.close()
 
    if not produto:
        redirect('/produtos?erro=Produto+não+encontrado.')
 
    return template('produto_editar', produto=produto)
 
@post('/produtos/editar/<id:int>')
def salvar_edicao_produto(id):
    nome = (request.forms.getunicode('nome') or '').strip()
    
    try:
        preco = float(request.forms.get('preco', 0))
        estoque = int(request.forms.get('estoque', 0))
    except ValueError:
        redirect('/produtos?erro=Preço+ou+estoque+inválidos.')
 
    if not nome or preco < 0 or estoque < 0:
        redirect('/produtos?erro=Valores+inválidos+para+atualização.')
 
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE produtos SET nome = ?, preco = ?, estoque = ? WHERE id = ?;", (nome, preco, estoque, id))
        conn.commit()
        redirect('/produtos')
    except sqlite3.Error as e:
        conn.rollback()
        redirect(f'/produtos?erro=Erro+ao+atualizar+produto:+{e}')
    finally:
        conn.close()
 
@get('/produtos/deletar/<id:int>')
def deletar_produto(id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = ?;", (id,))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()
    finally:
        conn.close()
    redirect('/produtos')
 
if __name__ == '__main__':
    inicializar_banco()
    print("Servidor rodando em http://localhost:8080 ...")
    run(host='localhost', port=8080, debug=True, reloader=True)