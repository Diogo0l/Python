# Versão refatorada e mais limpa
LIMITE_DESCONTO = 100
PERCENTUAL_DESCONTO = 0.1

def calcular_desconto(valor):
    if valor < 0:
        raise ValueError("O valor não pode ser negativo.")
    if valor > LIMITE_DESCONTO:
        return valor * PERCENTUAL_DESCONTO
    return 0