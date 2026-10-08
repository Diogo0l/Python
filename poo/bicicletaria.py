"""
João tem uma bicicletaria e deseja um programa para registrar e exibir as bicicletas vendidas. Cada bicicleta possui características próprias e é capaz de executar alguns comportamentos básicos.

Características (Atributos): Cor, modelo, ano e valor.
Comportamentos (Métodos): Buzinar, parar e correr.
"""

class Bicicleta:
    quantidade = 0
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        Bicicleta.quantidade += 1

def buzinar(self):
    print("Plim plim!")

def parar(self):
    print("Bicicleta parada.")

def correr(self):
    print("Vrummmm!")

'''b1 = Bicicleta("Vermelha", "Caloi", 2022, 600)
b2 = Bicicleta("Azul", "Monark", 2000, 189)

# Chamando os comportamentos (métodos)
b1.buzinar()
b1.correr()
b1.parar()
 
# Acessando atributos diretamente
print(b1.cor) # Saída: Vermelha
print(b2.modelo) # Saída: Monark'''

def Menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar bicicleta")
        print("2. Exibir bicicletas cadastradas")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cor = input("Digite a cor da bicicleta: ")
            modelo = input("Digite o modelo da bicicleta: ")
            ano = int(input("Digite o ano da bicicleta: "))
            valor = float(input("Digite o valor da bicicleta: "))
            bicicleta = Bicicleta(cor, modelo, ano, valor)  # noqa: F841
            print("Bicicleta cadastrada com sucesso!")
        elif opcao == "2":
            print(f"Quantidade de bicicletas cadastradas: {Bicicleta.quantidade}")
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
def main():
    Menu()



if __name__ == "__main__":
    main()