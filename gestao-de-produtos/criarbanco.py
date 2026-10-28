import sqlite3
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

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

query_campeao = """
SELECT
    p.id_produto,
    p.nome AS produto,
    c.nome_categoria AS categoria,
    SUM(v.quantidade) AS total_unidades_vendidas,
    SUM(v.quantidade * p.preco) AS faturamento_total
FROM Vendas v
INNER JOIN Produto p ON v.id_produto = p.id_produto
INNER JOIN Categoria c ON p.id_categoria = c.id_categoria
GROUP BY p.id_produto, p.nome, c.nome_categoria
ORDER BY total_unidades_vendidas DESC
LIMIT 1;
"""
 
cursor.execute(query_campeao)
resultado = cursor.fetchone()
 
if resultado:
    id_p, nome, categoria, total_qtd, faturamento = resultado
    print("\n--- PRODUTO MAIS VENDIDO ---")
    print(f"Produto: {nome} (ID: {id_p})")
    print(f"Categoria: {categoria}")
    print(f"Unidades vendidas: {total_qtd}")
    print(f"Faturamento gerado: R$ {faturamento:.2f}")


query_ranking = """
SELECT
    p.nome AS Produto,
    c.nome_categoria AS Categoria,
    p.preco AS Preco_Unitario,
    SUM(v.quantidade) AS Qtd_Vendida,
    SUM(v.quantidade * p.preco) AS Faturamento_Total,
    p.estoque AS Estoque_Restante
FROM Produto p
LEFT JOIN Vendas v ON p.id_produto = v.id_produto
LEFT JOIN Categoria c ON p.id_categoria = c.id_categoria
GROUP BY p.id_produto, p.nome, c.nome_categoria
ORDER BY Qtd_Vendida DESC;
"""
 
df_vendas = pd.read_sql_query(query_ranking, conn)
 
# Produtos sem nenhuma venda aparecem com NULL; troque por zero
df_vendas["Qtd_Vendida"] = df_vendas["Qtd_Vendida"].fillna(0).astype(int)
df_vendas["Faturamento_Total"] = df_vendas["Faturamento_Total"].fillna(0.0)
 
print("\n--- RANKING DE VENDAS POR PRODUTO ---")
print(df_vendas.to_string(index=False))

sns.set_theme(style="whitegrid")
 
# Cores: destaque para o líder, tom neutro para os demais
DESTAQUE, NEUTRA = "#1f4e79", "#9ab7d3"
paleta = {
    produto: (DESTAQUE if i == 0 else NEUTRA)
    for i, produto in enumerate(df_vendas["Produto"])
}
 
fig, ax = plt.subplots(figsize=(10, 5))
 
sns.barplot(
    data=df_vendas,
    x="Qtd_Vendida",
    y="Produto",
    hue="Produto",
    palette=paleta,
    legend=False,
    ax=ax,
)
 
lider = df_vendas.iloc[0]
ax.set_title(
    f"{lider['Produto']} lidera em volume com {lider['Qtd_Vendida']} unidades vendidas",
    fontsize=13, fontweight="bold", pad=15,
)
ax.set_xlabel("Quantidade de unidades vendidas", fontsize=11)
ax.set_ylabel("")
 
# Rótulo numérico ao lado de cada barra
for barra in ax.patches:
    largura = barra.get_width()
    if largura > 0:
        ax.annotate(
            f"{int(largura)} un.",
            (largura, barra.get_y() + barra.get_height() / 2),
            ha="left", va="center",
            xytext=(6, 0), textcoords="offset points",
            fontsize=10, fontweight="bold",
        )
 
sns.despine(top=True, right=True)
plt.tight_layout(pad=1.5)
 
# Salve ANTES de plt.show(), que pode limpar a figura
Path("static").mkdir(exist_ok=True)
plt.savefig("gestao-de-produtos/static/ranking_vendas.png", dpi=150, bbox_inches="tight")
plt.show()
 
conn.commit()

cursor.close()
conn.close()
print("Conexão encerrada com segurança.")