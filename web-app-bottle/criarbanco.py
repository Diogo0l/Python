
import sqlite3

DB_NAME = "cadastroClientes.db"

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    );
""")

conn.commit()
conn.close()

print("Tabela clientes criada com sucesso!")