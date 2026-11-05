from bottle import get, post, request, response, run


@get('/login')
def login():
    return """
        <h2>Login</h2>
        <form action="/login" method="POST">
            <label>Usuário:</label>
            <input type="text" name="username" required>
            <br><br>

            <label>Senha:</label>
            <input type="password" name="password" required>
            <br><br>

            <button type="submit">Entrar</button>
        </form>
    """


@post('/login')
def Login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if username == 'admin' and password == 'password':
        response.set_cookie(
            'account',
            username,
            secret='some-secret-key',
            httponly=True
        )
        return "Login efetuado!"
    else:
        return "Usuário ou senha inválido."


@get('/restrita')
def restricted():
    account = request.get_cookie(
        'account',
        secret='some-secret-key'
    )

    if account:
        return f"Welcome, {account}!"
    else:
        return """
            Acesso negado.
            Por favor, faça login novamente!
            <a href='/login'>Login</a>
        """


@get('/')
def hello():
    return """
        Bem-vindo à página inicial!
        <a href='/restrita'>Ir para a página restrita</a>
    """


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reload=True)