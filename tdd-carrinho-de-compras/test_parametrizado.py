import pytest
from carrinho import CarrinhoDeCompras


@pytest.mark.parametrize(
    "itens, total_esperado",
    [
        ([("Livro", 45.0), ("Caneta", 5.0)], 50.0),
        ([("Caderno", 15.0)], 15.0),
        ([], 0.0),
    ]
)
def test_calcular_total_com_diferentes_itens(itens, total_esperado):
    carrinho = CarrinhoDeCompras()
    for nome, preco in itens:
        carrinho.adicionar_item(nome, preco)
    assert carrinho.calcular_total() == total_esperado
    
    
@pytest.mark.parametrize(
    "itens_iniciais, item_remover, tamanho_esperado",
    [
        ([("Livro", 45.0), ("Caneta", 5.0)], "Livro", 1),
        ([("Caderno", 15.0)], "Caderno", 0),
    ]
)
def test_remover_varios_itens(itens_iniciais, item_remover, tamanho_esperado):
    carrinho = CarrinhoDeCompras()
    for nome, preco in itens_iniciais:
        carrinho.adicionar_item(nome, preco)
    
    carrinho.remover_item(item_remover)
    
    assert len(carrinho.itens) == tamanho_esperado
 