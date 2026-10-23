<h2>Gestão de Clientes</h2>
 
% if get('msg_erro', ''):
    <div class="alerta">⚠️ {{ msg_erro }}</div>
% end

<style>
    :root {
        --primary-color: #0d6efd;
        --success-color: #198754;
        --danger-color: #dc3545;
        --bg-color: #f8f9fa;
        --card-bg: #ffffff;
        --text-color: #212529;
        --border-color: #dee2e6;
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

    header {
        background-color: var(--primary-color);
        color: white;
        padding: 1rem 2rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    header h1 {
        margin: 0;
        font-size: 1.5rem;
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

    .alerta {
        background-color: #f8d7da;
        color: #842029;
        border: 1px solid #f5c2c7;
        padding: 12px;
        border-radius: 6px;
        margin-bottom: 20px;
    }

    form {
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
        background-color: var(--success-color);
        color: white;
        border: none;
        padding: 12px 20px;
        cursor: pointer;
        border-radius: 5px;
        font-size: 16px;
        transition: background-color 0.2s;
    }

    input[type="submit"]:hover {
        background-color: #157347;
    }

    hr {
        border: 0;
        border-top: 1px solid var(--border-color);
        margin: 30px 0;
    }

    .tabela-container {
        width: 100%;
        overflow-x: auto;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        background-color: white;
    }

    thead tr {
        background-color: var(--primary-color);
        color: white;
    }

    th,
    td {
        padding: 14px 12px;
        text-align: left;
        border-bottom: 1px solid var(--border-color);
    }

    th {
        font-weight: bold;
        white-space: nowrap;
    }

    tbody tr:hover {
        background-color: #f1f5f9;
    }

    .acao {
        display: inline-block;
        margin-right: 10px;
        text-decoration: none;
        font-weight: bold;
    }

    .editar {
        color: var(--primary-color);
    }

    .excluir {
        color: var(--danger-color);
    }

    .acao:hover {
        text-decoration: underline;
    }

    footer {
        text-align: center;
        padding: 20px;
        font-size: 0.85rem;
        color: #6c757d;
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

        th,
        td {
            padding: 10px 8px;
            font-size: 13px;
        }

        input[type="submit"] {
            width: 100%;
        }
    }
</style>

<main>
    <h2>Cadastrar Novo Cliente</h2>

    % if get('msg_erro', ''):
        <div class="alerta">
            ⚠️ {{ msg_erro }}
        </div>
    % end

    <form action="/cadastrar" method="post">
        <div class="campo">
            <label for="nome">Nome:</label>
            <input
                type="text"
                id="nome"
                name="nome"
                placeholder="Digite o nome completo"
                required
            >
        </div>

        <div class="campo">
            <label for="email">E-mail:</label>
            <input
                type="email"
                id="email"
                name="email"
                placeholder="Ex: nome@gmail.com"
                required
            >
        </div>

        <input type="submit" value="Salvar Cliente">
    </form>

    <hr>

    <h2>Clientes Cadastrados</h2>

    <div class="tabela-container">
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>E-mail</th>
                    <th>Ações</th>
                </tr>
            </thead>

            <tbody>
                % for id_, nome, email in lista_clientes:
                <tr>
                    <td>{{ id_ }}</td>
                    <td>{{ nome }}</td>
                    <td>{{ email }}</td>
                    <td>
                        <a
                            href="/editar/{{ id_ }}"
                            class="acao editar"
                        >Editar</a>

                        <a
                            href="/deletar/{{ id_ }}"
                            class="acao excluir"
                        >Excluir</a>
                    </td>
                </tr>
                % end
            </tbody>
        </table>
    </div>
</main>
