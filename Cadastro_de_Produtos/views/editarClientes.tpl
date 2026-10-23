
<style>
    :root {
        --primary-color: #0d6efd;
        --success-color: #198754;
        --bg-color: #f8f9fa;
        --card-bg: #ffffff;
        --text-color: #212529;
    }

    * {
        box-sizing: border-box;
    }

    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: var(--bg-color);
        color: var(--text-color);
        margin: 0;
        padding: 20px;
    }

    main {
        max-width: 1100px;
        width: 100%;
        margin: 30px auto;
        padding: 25px;
        background: var(--card-bg);
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }

    h2 {
        margin-top: 0;
        margin-bottom: 25px;
        font-size: 1.7rem;
    }

    form {
        max-width: 400px;
        margin-bottom: 30px;
    }

    .campo {
        margin-bottom: 18px;
    }

    .campo label {
        display: block;
        margin-bottom: 7px;
        font-weight: 500;
    }

    .campo input {
        display: block;
        width: 100%;
        padding: 12px;
        border: 1px solid #ced4da;
        border-radius: 5px;
        font-size: 16px;
        background-color: white;
        color: var(--text-color);
        outline: none;
    }

    .campo input:focus {
        border-color: #86b7fe;
        box-shadow: 0 0 0 3px rgba(13, 110, 253, 0.2);
    }

    input[type="submit"] {
        background-color: var(--primary-color);
        color: white;
        border: none;
        padding: 10px 15px;
        cursor: pointer;
        border-radius: 4px;
        font-size: 16px;
    }

    input[type="submit"]:hover {
        background-color: #0b5ed7;
    }

    .cancelar {
        margin-left: 10px;
        color: #6c757d;
        text-decoration: none;
    }

    .cancelar:hover {
        text-decoration: underline;
    }

    @media (max-width: 600px) {
        body {
            padding: 10px;
        }

        main {
            margin: 10px auto;
            padding: 15px;
        }

        h2 {
            font-size: 1.4rem;
        }

        form {
            max-width: 100%;
        }

        input[type="submit"] {
            width: 100%;
        }

        .cancelar {
            display: inline-block;
            margin: 15px 0 0;
        }
    }
</style>

<main>
    <h2>Editar Cliente</h2>

    <form action="/editar/{{ cliente[0] }}" method="post">
        <div class="campo">
            <label for="nome">Nome:</label>
            <input
                type="text"
                id="nome"
                name="nome"
                value="{{ cliente[1] }}"
                required
            >
        </div>

        <div class="campo">
            <label for="email">E-mail:</label>
            <input
                type="email"
                id="email"
                name="email"
                value="{{ cliente[2] }}"
                required
            >
        </div>

        <input type="submit" value="Atualizar">

        <a href="/" class="cancelar">Cancelar</a>
    </form>
</main>