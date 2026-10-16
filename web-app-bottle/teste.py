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

    return template('web-app-bottle/views/clientes_template', lista_clientes=lista_clientes)


run(host="localhost", port=8080)
