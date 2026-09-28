"""Operação de extrato
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.

Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:

1500.45 = R$ 1500.45"""

def exibir_extrato(depositos, saques, saldo):
    if not depositos and not saques:
        print("Não foram realizadas movimentações.")
    else:
        print("Extrato:")
        for deposito in depositos:
            print(f"Depósito: R$ {deposito:.2f}")
        for saque in saques:
            print(f"Saque: R$ {saque:.2f}")
    print(f"Saldo atual: R$ {saldo:.2f}")
    
# Teste da função de extrato
depositos_realizados = [1000.0, 500.0]  # Lista de depósitos realizados
saques_realizados = [200.0, 300.0]  # Lista de saques realizados
saldo_atual = 1000.0  # Saldo atual da conta bancária

exibir_extrato(depositos_realizados, saques_realizados, saldo_atual)