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