'''
Iteração: Utilize um laço 'for' junto com metódo .items() para imprimir cada chave e valor do dicionário alunos no formato: Chave X - Dados Y.
'''

alunos = {
    "nome": "Diogo",
    "idade": 18,
    "curso": "Programador de Sistemas"
}

for chave, valor in alunos.items():
    print(f"Chave: {chave} - Dados: {valor}")