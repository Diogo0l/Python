"""
Crie um app que mostre no console a média de 3 notas.
Usando o Exemplo de Listar Notas, crie um app com janelas em Python para receber 3 notas e mostrar a média.

Algoritmo: 
- [ ] Receber 3 notas do usuário
- [ ] Calcular a média das notas
- [ ] Mostrar a média no console
- [ ] Criar as funções
- [ ] Criar a janela
"""

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"A média das notas é {media:.2f}. \nAluno Aprovado!")
else:
    print(f"A média das notas é {media:.2f}. \nAluno Reprovado!")