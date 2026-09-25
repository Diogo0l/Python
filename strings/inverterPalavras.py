'''
Inverter ordem das palavras
- Escreva um algoritmo que inverte a ordem das palavras em uma frase.
'''

frase = input("Digite uma frase: ")

palavras = frase.split()
palavras.reverse()

print(" ".join(palavras))
