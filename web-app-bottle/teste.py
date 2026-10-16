from bottle import route, run, template


@route("/")
def teste():
    
    lista_clientes = [
        {
            "nome": "Diogo",
            "email": "diogo@gmail.com",
            "ativo": True
        }
    ]

    page = """
    <ul>
        % for cliente in lista_clientes:
            % if cliente['ativo']:
                <li><strong>{{ cliente['nome'] }}</strong> - {{ cliente['email'] }}</li>
            % else:
                <li style="color: gray;">{{ cliente['nome'] }} (Inativo)</li>
            % end
        % end
    </ul>
"""

    return template(page, lista_clientes=lista_clientes)


run(host="localhost", port=8080)
