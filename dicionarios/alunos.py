'''
Criação: Crie um dicionário chamado alunos que contenha 3 alunos como chaves e seus respectivos dicionários internos com nome, idade e curso.
'''

aluno1 = {
    "nome": "Diogo",
    "idade": 18,
    "curso": "Programador de Sistemas"
}

aluno2 = {
    "nome": "João",
    "idade": 19,
    "curso": "Engenharia de Software"
}

aluno3 = {
    "nome": "Pedro",
    "idade": 20,
    "curso": "Administração"
}

alunos = {
    
}

print(f"O primeiro aluno é {aluno1}")
print(f"O segundo aluno é {aluno2}")
print(f"O terceiro aluno é {aluno3}")


"""
Segunda forma de fazer um dicionário de alunos com listas de valores para cada chave.

alunos = {
    "nome": ["Diogo", "João", "Pedro"],
    "idade": [18],
    "curso": ["Programador de Sistemas"]
}

print(alunos["nome"], alunos["idade"], alunos["curso"])"""