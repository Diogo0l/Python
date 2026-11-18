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
    
def test_carrinho_vazio_deve_retornar_total_zero():
    carrinho = CarrinhoDeCompras()
    assert carrinho.calcular_total() == 0.0
 
def test_deve_remover_item_do_carrinho():
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("Livro", 45.0)
    
    carrinho.remover_item("Livro")
    
    assert len(carrinho.itens) == 0
 
def test_deve_atualizar_preco_do_item():
    carrinho = CarrinhoDeCompras()
    carrinho.adicionar_item("Livro", 45.0)
    
    # Chamamos o método que vamos criar para atualizar o preço
    carrinho.atualizar_preco("Livro", 50.0)
    
    # O que devemos verificar aqui para garantir que o preço mudou para 50.0?
    assert carrinho.itens[0]["preco"] == 50.0, "Erro: O preço do item não foi atualizado corretamente."