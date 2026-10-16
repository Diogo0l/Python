
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Cadastrar Cliente</title>
</head>
<body>
    <h1>Cadastrar Cliente</h1>

    <form action="/cadastrar" method="post">
        <label for="nome">Nome:</label>
        <input
            type="text"
            id="nome"
            name="nome"
            required
        >

        <br><br>

        <label for="email">E-mail:</label>
        <input
            type="email"
            id="email"
            name="email"
            required
        >

        <br><br>

        <button type="submit">Cadastrar</button>
    </form>

    <br>

    <a href="/">Voltar para a lista de clientes</a>
</body>
</html>
