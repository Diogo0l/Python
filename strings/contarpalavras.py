'''
Contar palavras em uma frase
Escreva um algoritmo que conta o número de palavras em uma frase.

[x] - Recebe uma frase de um usuário.
[x] - Conta o número de palavras na frase.
[x] - Mostra quantas palavras a frase tem.
'''

frase = input("Digite uma frase: ")

palavras = frase.split()
quantidade = len(palavras)

print(f"A frase contém {quantidade} palavras!")
