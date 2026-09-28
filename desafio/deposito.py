"""Operação de depósito bancário.

Deve ser possível depositar valoers positivos para a minha conta bancária. 
A vi do projeto trabalha apenas com 1 usuários, dessa forma não precisamos nos preocupar em identificar qual número da agência e conta bancária.
Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato bancário.
"""

# Função de depósito bancário. Args: valor (float): Valor a ser depositado. saldo (float): Saldo atual da conta bancária. Retorna: float: Novo saldo após o depósito.
def depositar(valor, saldo):
    if valor > 0:
        saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    else:
        print("Valor inválido. Por favor, insira um valor maior que zero.")
        
        return saldo
    
# Saldo atual da conta bancária
saldo_atual = 0.0
deposito_valor = float(input("Digite o valor a ser depositado: "))
saldo_atual = depositar(deposito_valor, saldo_atual) 
print(f"Saldo: {saldo_atual:.2f}")
