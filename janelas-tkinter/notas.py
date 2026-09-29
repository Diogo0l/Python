"""
Crie um app que mostre no console a média de 3 notas.
Usando o Exemplo de Listar Notas, crie um app com janelas em Python para receber 3 notas e mostrar a média.

Algoritmo: 
- [x] Receber 3 notas do usuário
- [x] Calcular a média das notas
- [x] Mostrar a média no console
- [x] Criar as funções
- [x] Criar a janela
"""

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"A média das notas é {media:.2f}. \nAluno Aprovado!")
else:
    print(f"A média das notas é {media:.2f}. \nAluno Reprovado!")