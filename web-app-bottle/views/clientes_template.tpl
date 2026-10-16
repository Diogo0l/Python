<ul>
    % for cliente in lista_clientes:
        % if cliente['ativo']:
            <li><strong>{{ cliente['nome'] }}</strong> - {{ cliente['email'] }}</li>
        % else:
            <li style="color: gray;">{{ cliente['nome'] }} (Inativo)</li>
        % end
    % end
</ul>