% rebase('base.tpl', titulo='Gestão de Produtos')
 
<h2>Cadastro de Produtos</h2>
 
% if get('msg_erro', ''):
    <div class="alerta">⚠️ {{ msg_erro }}</div>
% end
 
<form class="card" action="/produtos/cadastrar" method="post">
    <label>Nome do Produto:</label>
    <input type="text" name="nome" required placeholder="Ex: Notebook, Mouse...">
 
    <label>Preço (R$):</label>
    <input type="number" step="0.01" name="preco" required placeholder="0.00">
 
    <label>Estoque Inicial:</label>
    <input type="number" name="estoque" required placeholder="0" value="0">
 
    <input type="submit" value="Cadastrar Produto">
</form>
 
<hr>
 
<h2>Produtos em Estoque</h2>
% if not lista_produtos:
    <p>Nenhum produto cadastrado até o momento.</p>
% else:
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Preço</th>
                <th>Estoque</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            % for p in lista_produtos:
            <tr>
                <td>{{ p['id'] }}</td>
                <td>{{ p['nome'] }}</td>
                <td>R$ {{ "%.2f" % p['preco'] }}</td>
                <td>{{ p['estoque'] }} unid.</td>
                <td>
                    <a class="btn-edit" href="/produtos/editar/{{ p['id'] }}">Editar</a>
                    <a class="btn-del" href="/produtos/deletar/{{ p['id'] }}" onclick="return confirm('Deseja excluir este produto?');">Excluir</a>
                </td>
            </tr>
            % end
        </tbody>
    </table>
% end