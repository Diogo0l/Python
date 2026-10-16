'''Esse arquivo cria um banco de dados chamado "cadastroClientes.db" e cria nesse arquivo, a tabela clientes. Para rodar: python criarbanco.py'''
import sqlite3

DB_NAME = "cadastroClientes.db"

# 1. Abre a conexão com o arquivo do banco de dados (ou cria se não existir)
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor() # <- 2. Cria o objeto cursor para enviar comandos SQL

# Executa a criação da tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    );
""")

# Confirma a alteração estrutural no banco
conn.commit()
conn.close()

print("Tabela clientes criada com sucesso!")