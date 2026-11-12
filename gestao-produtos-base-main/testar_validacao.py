from validacao import validar_produto

CATEGORIAS = {1, 2, 3}

dados, erros =  validar_produto(
    {"nome": "Produto A", "preco": 10.0, "estoque": 5, "id_categoria": 1},
    CATEGORIAS,
)

assert erros == {}
assert dados == {"nome": "Produto A", "preco": 10.0, "estoque": 5, "id_categoria": 1}

assert erros != {}
assert dados == {}

print("Todos os testes passaram com sucesso!")
