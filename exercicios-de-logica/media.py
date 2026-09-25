'''
Algoritmo de média, que mostra se o aluno foi aprovado ou reprovado.
'''

nota1 = float(input("Digite o valor da 1° nota: "))
nota2 = float(input("Digite o valor da 2° nota: "))
nota3 = float(input("Digite o valor da 3° nota: "))

media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print("O aluno foi Aprovado!")
else:
    print("O aluno foi Reprovado!")

print(f"A média do aluno é: {media:.2f}")

# ":.2f" depois da variável media, serve para limitar as casas decimais.