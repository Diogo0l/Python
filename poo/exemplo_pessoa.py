class Pessoa:

    populacao = 0
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa.populacao += 1

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

    def __str__(self):
        return f"Pessoa(nome={self.nome}, idade={self.idade})"

    def __del__(self):
        Pessoa.populacao -= 1
        print(f"{self.nome} foi removido da população.")

pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)
print(pessoa1.apresentar())
print(pessoa2.apresentar())
print(pessoa1)
print(pessoa2)
print(f"População: {Pessoa.populacao}")