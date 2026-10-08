class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return (f"{self.nome} late.")

class Gato(Animal):
    def fazer_som(self):
        return (f"{self.nome} mia.")

class Quimera(Cachorro, Gato):
    def fazer_som(self):
        return (f"{self.nome} faz um som estranho: {Cachorro.fazer_som(self)} e {Gato.fazer_som(self)}")

Meu_cachorro = Cachorro("Totó")
Meu_gato = Gato("Xaninho")
print(Meu_cachorro.fazer_som())
print(Meu_gato.fazer_som())
gato_de_rua = Quimera("Gato de Rua")
print(gato_de_rua.fazer_som())

# Exemplo de polimorfismo
def animal_faz_som(animal):
    print('-' * 20)
    print(f"{animal.nome} {animal.fazer_som()}")

animal_faz_som(Meu_cachorro)
animal_faz_som(Meu_gato)
animal_faz_som(gato_de_rua)