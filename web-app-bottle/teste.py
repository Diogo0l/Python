from bottle import route, run, template


@route("/")
def teste(name="World"):

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

    return template("hello_template", page, name=name)


run(host="localhost", port=8080)
