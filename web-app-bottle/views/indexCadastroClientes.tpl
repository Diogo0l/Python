% rebase('web-app-bottle/views/baseCadastroClientes.tpl', titulo='Listagem de Clientes')
 
<h2>Cadastrar Novo Cliente</h2>
 
% if get('msg_erro', ''):
    <div class="alerta">⚠️ {{ msg_erro }}</div>
% end
 
<form action="/cadastrar" method="post" style="margin-bottom: 30px;">
    <div style="margin-bottom: 10px;">
        <label style="display:block;">Nome:</label>
        <input type="text" name="nome" required style="width: 100%; padding: 8px; box-sizing: border-box;">
    </div>
 
    <div style="margin-bottom: 10px;">
        <label style="display:block;">E-mail:</label>
        <input type="email" name="email" required style="width: 100%; padding: 8px; box-sizing: border-box;">
    </div>

    <div style="margin-bottom: 10px;">
        <label style="display:block;">Telefone:</label>
        <input type="telefone" name="telefone" required style="width: 100%; padding: 8px; box-sizing: border-box;">
    </div>
 
    <input type="submit" value="Salvar Cliente" style="background: var(--success-color); color: white; border: none; padding: 10px 15px; cursor: pointer; border-radius: 4px;">
</form>
 
<hr>
 
<h2>Clientes Cadastrados</h2>
<table style="width: 100%; border-collapse: collapse;">
    <thead>
        <tr style="background: #0d6efd; text-align: left; color: white;">
            <th style="padding: 10px; border-bottom: 2px solid #dee2e6;">ID</th>
            <th style="padding: 10px; border-bottom: 2px solid #dee2e6;">Nome</th>
            <th style="padding: 10px; border-bottom: 2px solid #dee2e6;">E-mail</th>
            <th style="padding: 10px; border-bottom: 2px solid #dee2e6;">Telefone</th>
            <th style="padding: 10px; border-bottom: 2px solid #dee2e6;">Ações</th>
        </tr>
    </thead>
    <tbody>
        % for id_, nome, email, telefone in lista_clientes:
        <tr style="border-bottom: 1px solid #dee2e6;">
            <td style="padding: 10px;">{{ id_ }}</td>
            <td style="padding: 10px;">{{ nome }}</td>
            <td style="padding: 10px;">{{ email }}</td>
            <td style="padding: 10px;">{{ telefone }}</td>
            <td style="padding: 10px;">
                <a href="/editar/{{ id_ }}" style="color: var(--primary-color); font-weight: bold; margin-right: 10px; text-decoration: none;">Editar</a>
                <a href="/deletar/{{ id_ }}" style="color: var(--danger-color); font-weight: bold; text-decoration: none;">Excluir</a>
            </td>
        </tr>
        % end
    </tbody>
</table>

<!--  --!>