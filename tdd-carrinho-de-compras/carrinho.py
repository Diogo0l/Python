class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []
        
    def adicionar_item(self, nome, preco):
        self.itens.append((nome, preco))

    def calcular_total(self):
        return sum(preco for _, preco in self.itens)
    
carrinho = CarrinhoDeCompras()