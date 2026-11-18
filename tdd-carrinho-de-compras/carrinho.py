class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, nome, preco):
        item = {"nome": nome, "preco": preco}
        self.itens.append(item)


    def calcular_total(self):
        total = 0
        for item in self.itens:
            total += item["preco"]
        return total
        #return sum(item['preco'] for item in self.itens)
    
    
    def remover_item(self, nome):
        novos_itens = []
        for item in self.itens:
            if item["nome"] != nome:
                novos_itens.append(item)
        self.itens = novos_itens


    def atualizar_preco(self, nome, novo_preco):
        for item in self.itens:
            if item["nome"] == nome:
                item["preco"] = novo_preco
                break