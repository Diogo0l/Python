import sqlite3

import pandas as pd
 
# Abre (ou cria) o banco de dados local
conn = sqlite3.connect("gestao-de-produtos/gestao_produtos.db")
 
# O cursor envia comandos SQL e recebe os resultados
cursor = conn.cursor()
 
print("Conexão estabelecida com sucesso!")

# O SQLite só verifica chaves estrangeiras se você pedir, a cada conexão
cursor.execute("PRAGMA foreign_keys = ON;")
 
cursor.executescript('''
DROP TABLE IF EXISTS Vendas;
DROP TABLE IF EXISTS Produto;
DROP TABLE IF EXISTS Categoria;
 
CREATE TABLE Categoria (
    id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_categoria TEXT NOT NULL
);
 
CREATE TABLE Produto (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL CHECK(preco >= 0.0),
    estoque INTEGER NOT NULL CHECK(estoque >= 0),
    id_categoria INTEGER,
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
);

CREATE TABLE Vendas (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produto INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK (quantidade >= 0),
    data_venda TEXT NOT NULL DEFAULT (datetime('now', 'localtime')),
    FOREIGN KEY (id_produto) REFERENCES Produto(id_produto)
);
''')
 
conn.commit()
print("Tabelas 'Categoria', 'Produto' e 'Vendas' criadas com sucesso!")

categorias_iniciais = [
    ("Eletrônicos",),
    ("Móveis",),
    ("Vestuário",),
]
 
# (nome, preço, estoque, id_categoria)
produtos_iniciais = [
    ("Smartphone", 1500.00, 10, 1),
    ("Notebook", 3500.00, 5, 1),
    ("Sofá", 800.00, 3, 2),
    ("Cadeira de Escritório", 350.00, 12, 2),
    ("Camisa Polo", 80.00, 25, 3),
    ("Calça Jeans", 120.00, 15, 3),
]
 
cursor.executemany(
    "INSERT INTO Categoria (nome_categoria) VALUES (?);", categorias_iniciais
)
cursor.executemany(
    "INSERT INTO Produto (nome, preco, estoque, id_categoria) VALUES (?, ?, ?, ?);",
    produtos_iniciais
)
 
conn.commit()
print(f"{len(categorias_iniciais)} categorias e {len(produtos_iniciais)} produtos inseridos.")

cursor.execute("SELECT id_produto, nome, preco, estoque FROM Produto;")
linhas = cursor.fetchall()
 
print("\n--- Lista de Produtos Cadastrados ---")
for id_p, nome, preco, estoque in linhas:
    print(f"ID: {id_p} | Produto: {nome} | Preço: R$ {preco:.2f} | Estoque: {estoque}")
    
# 1. Atualizar o preço de um produto
cursor.execute(
    "UPDATE Produto SET preco = ? WHERE nome = ?;", (1600.00, "Smartphone")
)
print("Linhas atualizadas:", cursor.rowcount)
 
# 2. Excluir um produto
cursor.execute("DELETE FROM Produto WHERE nome = ?;", ("Calça Jeans",))
print("Linhas excluídas:", cursor.rowcount)

def registrar_venda(conn, id_produto, quantidade):
    """Baixa o estoque e registra a venda na mesma transação."""
    with conn:  # commit se der certo, rollback se der erro
        conn.execute(
            "UPDATE Produto SET estoque = estoque - ? WHERE id_produto = ?;",
            (quantidade, id_produto),
        )
        conn.execute(
            "INSERT INTO Vendas (id_produto, quantidade) VALUES (?, ?);",
            (id_produto, quantidade),
        )
 
 
novas_vendas = [(1, 3), (2, 2), (1, 4), (3, 1), (4, 5), (5, 10)]
 
for id_produto, quantidade in novas_vendas:
    try:
        registrar_venda(conn, id_produto, quantidade)
    except sqlite3.IntegrityError as erro:
        print(f"Venda recusada ({id_produto}, {quantidade}): {erro}")
 
print("Processamento de vendas concluído.")
 
conn.commit()

cursor.close()
conn.close()
print("Conexão encerrada com segurança.")