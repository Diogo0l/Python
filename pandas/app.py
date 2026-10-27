import sqlite3

import pandas as pd


# Salvando os arquivos CSV (encoding utf-8 para não quebrar os acentos)
def criar_alunos_csv():
    with open("pandas/alunos.csv", "w", encoding="utf-8") as f:
        f.write(
            "id_aluno,nome_aluno,idade,cidade\n"
            "1,Ana Silva,21,São Paulo\n"
            "2,Bruno Costa,24,Rio de Janeiro\n"
            "3,Carlos Souza,19,Belo Horizonte\n"
            "4,Diana Martins,22,São Paulo\n"
            "5,Eduardo Lima,20,Fortaleza\n"
        )

def criar_cursos_csv():
    with open("pandas/cursos.csv", "w", encoding="utf-8") as f:
        f.write(
            "id_curso,nome_curso,preco_mensalidade\n"
            "101,Python para Dados,150\n"
            "102,Web Design Moderno,120\n"
            "103,Banco de Dados SQL,130\n"
        )

def criar_matriculas_csv():
    with open("pandas/matriculas.csv", "w", encoding="utf-8") as f:
        f.write(
            "id_matricula,id_aluno,id_curso,status\n"
            "1001,1,101,Ativo\n"
            "1002,1,103,Ativo\n"
            "1003,2,101,Ativo\n"
            "1004,3,102,Cancelado\n"
            "1005,4,101,Ativo\n"
            "1006,4,103,Trancado\n"
        )

def mostrar_csvs():
    alunos = pd.read_csv("pandas/alunos.csv", encoding="utf-8")
    cursos = pd.read_csv("pandas/cursos.csv", encoding="utf-8")
    matriculas = pd.read_csv("pandas/matriculas.csv", encoding="utf-8")
    
    print(f"alunos: {alunos.shape} | cursos: {cursos.shape} | matriculas: {matriculas.shape}")
    print(matriculas["status"].value_counts())

def criar_db():
    conn = sqlite3.connect("pandas/escola.db")
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()
    
    cur.executescript("""
        DROP TABLE IF EXISTS matriculas;
        DROP TABLE IF EXISTS cursos;
        DROP TABLE IF EXISTS alunos;

        CREATE TABLE alunos (
            id_aluno INTEGER PRIMARY KEY,
            nome_aluno TEXT NOT NULL,
            idade INTEGER,
            cidade TEXT
        );

        CREATE TABLE cursos (
            id_curso INTEGER PRIMARY KEY,
            nome_curso TEXT NOT NULL,
            preco_mensalidade REAL NOT NULL
        );

        CREATE TABLE matriculas (
            id_matricula INTEGER PRIMARY KEY,
            id_aluno INTEGER NOT NULL REFERENCES alunos(id_aluno),
            id_curso INTEGER NOT NULL REFERENCES cursos(id_curso),
            status TEXT NOT NULL CHECK (status IN ('Ativo', 'Cancelado', 'Trancado'))
        );
    """)
    
    return conn, cur

# Ajustado para receber conn e cur como parâmetros
def inserir_alunos_db(conn, cur):  
    cur.executemany("INSERT INTO alunos VALUES (?,?,?,?)", [
        (1, 'Ana Silva', 21, 'São Paulo'),
        (2, 'Bruno Costa', 24, 'Rio de Janeiro'),
        (3, 'Carlos Souza', 19, 'Belo Horizonte'),
        (4, 'Diana Martins', 22, 'São Paulo'),
    ])
    
    cur.executemany("INSERT INTO cursos VALUES (?,?,?)", [
        (101, 'Python para Dados', 150),
        (102, 'Web Design Moderno', 120),
        (103, 'Banco de Dados SQL', 130),
    ])
    
    cur.executemany("INSERT INTO matriculas VALUES (?,?,?,?)", [
        (1001, 1, 101, 'Ativo'),
        (1002, 1, 103, 'Ativo'),
        (1003, 2, 101, 'Ativo'),
        (1004, 3, 102, 'Cancelado'),
        (1005, 4, 101, 'Ativo'),
    ])
    conn.commit()
    
conn, cur = criar_db()         # Cria o banco e guarda a conexão e o cursor
inserir_alunos_db(conn, cur)   # Passa a conexão e o cursor para inserir os dados
conn.close()                   # Fecha o banco de dados com segurança
print("Banco de dados criado e dados inseridos!")