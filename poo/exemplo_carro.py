class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo)
        self.ano = ano

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Ano: {self.ano}")


# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020)
meu_carro.exibir_informacoes()