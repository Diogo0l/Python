"""Operação de saque

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

- [ ] O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
- [ ] Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
- [ ] Verificar a quantidade de saques realizados.
- [ ] Verificar se o valor do saque é positivo e menor ou igual a R$ 500,00.
- [ ] Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.
"""

def sacar(valor, saldo, saques_realizados):
    if saques_realizados >= 3:
        print("Limite de saques diários atingido. Não é possível realizar mais saques hoje.")
        return saldo, saques_realizados

    if valor > 500:
        print("Valor do saque excede o limite máximo de R$ 500,00 por saque.")
        return saldo, saques_realizados

    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
        return saldo, saques_realizados
    
    if valor <= 0:
        print("Valor do saque deve ser maior que zero.")
        return saldo, saques_realizados

    saldo -= valor
    saques_realizados += 1
    print(f"Saque de R${valor:.2f} realizado com sucesso.")
    
    return saldo, saques_realizados

# Teste da função de saque
saldo_atual = 1000.0  # Saldo inicial da conta bancária
saques_realizados = 0  # Contador de saques realizados

while True:
    saque_valor = float(input("Digite o valor do saque (ou 0 para sair): "))
    if saque_valor == 0:
        break
    saldo_atual, saques_realizados = sacar(saque_valor, saldo_atual, saques_realizados)
    print(f"Saldo: {saldo_atual:.2f}")
    print(f"Saques realizados hoje: {saques_realizados}/3")