import pandas as pd

# Salvando os arquivos CSV (encoding utf-8 para não quebrar os acentos)
with open('pandas/alunos.csv', 'w', encoding='utf-8') as f:
    f.write(
        'id_aluno,nome_aluno,idade,cidade\n'
        '1,Ana Silva,21,São Paulo\n'
        '2,Bruno Costa,24,Rio de Janeiro\n'
        '3,Carlos Souza,19,Belo Horizonte\n'
        '4,Diana Martins,22,São Paulo\n'
        '5,Eduardo Lima,20,Fortaleza\n'
    )
 
with open('pandas/cursos.csv', 'w', encoding='utf-8') as f:
    f.write(
        'id_curso,nome_curso,preco_mensalidade\n'
        '101,Python para Dados,150\n'
        '102,Web Design Moderno,120\n'
        '103,Banco de Dados SQL,130\n'
    )
 
with open('pandas/matriculas.csv', 'w', encoding='utf-8') as f:
    f.write(
        'id_matricula,id_aluno,id_curso,status\n'
        '1001,1,101,Ativo\n'
        '1002,1,103,Ativo\n'
        '1003,2,101,Ativo\n'
        '1004,3,102,Cancelado\n'
        '1005,4,101,Ativo\n'
        '1006,4,103,Trancado\n'
    )
 
alunos = pd.read_csv('pandas/alunos.csv', encoding='utf-8')
cursos = pd.read_csv('pandas/cursos.csv', encoding='utf-8')
matriculas = pd.read_csv('pandas/matriculas.csv', encoding='utf-8')
 
# Sempre inspecione os dados depois de carregar
print(f'alunos: {alunos.shape} | cursos: {cursos.shape} | matriculas: {matriculas.shape}')
print(matriculas['status'].value_counts())