% rebase('Cadastro_de_Produtos/views/baseCadastroProdutos.tpl', titulo='Editar Produto')
 
<h2>Editar Produto #{{ produto['id'] }}</h2>
 
<form class="card" action="/produtos/editar/{{ produto['id'] }}" method="post">
    <label>Nome do Produto:</label>
    <input type="text" name="nome" value="{{ produto['nome'] }}" required>
 
    <label>Preço (R$):</label>
    <input type="number" step="0.01" name="preco" value="{{ produto['preco'] }}" required>
 
    <label>Estoque:</label>
    <input type="number" name="estoque" value="{{ produto['estoque'] }}" required>
 
    <input type="submit" value="Salvar Alterações">
    <a href="/produtos" style="margin-left: 10px; color: #6c757d; text-decoration: none;">Cancelar</a>
</form>