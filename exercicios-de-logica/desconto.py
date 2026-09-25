'''
Algoritmo que aplica um desconto em um valor.
'''

valor_produto = float(input("Digite o valor do produto: "))
desconto = int(input("Digite o desconto que deseja dar ao produto: "))

valor_final = valor_produto * (desconto / 100)

print(f"O valor do produto é {valor_produto}, com desconto fica: {valor_final}")