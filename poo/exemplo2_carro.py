class Veiculo:
    def mover(self):
        pass
 
class Carro(Veiculo):
    def mover(self):
        print("O carro está dirigindo")
 
class Aviao(Veiculo):
    def mover(self):
        print("O avião está voando")
 
# Usando polimorfismo
def acao_veiculo(veiculo):
    veiculo.mover()
 
meu_carro = Carro()
meu_aviao = Aviao()
 
acao_veiculo(meu_carro)
acao_veiculo(meu_aviao)