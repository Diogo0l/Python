"""Testa as funcionalidades do carrinho de compras:
- [ ] iniciar vazio
- [ ] adicionar item
- [ ] remover item
- [ ] calcular total
- [ ] atualizar preço"""

from carrinho import CarrinhoDeCompras


def test_carrinho_deve_iniciar_vazio():
    carrinho = CarrinhoDeCompras()
    assert len(carrinho.itens) == 0
    
def test_adicionar_item():
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("Livro", 45.0)
    assert len(carrinho.itens) == 1
    
def test_deve_calcular_preco_total_do_carrinho():
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("Livro", 45.0)
    carrinho.adicionar_item("Caneta", 5.0)
    
    assert carrinho.calcular_total() == 50.0
    
def remover_item(self, nome):
    novos_itens = []
    for item in self.itens:
        if item["nome"] != nome:
            novos_itens.append(item)
    self.itens = novos_itens
 