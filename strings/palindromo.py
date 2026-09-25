'''
Verificar palíndromo
- Escreva um algoritmo que verifica se uma string é um palíndromo.
'''

texto = input("Digite uma string: ")

if texto == texto[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")