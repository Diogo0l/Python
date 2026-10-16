<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ get('titulo', 'Sistema de Clientes') }}</title>
    <style>
        :root {
            --primary-color: #0d6efd;
            --success-color: #198754;
            --danger-color: #dc3545;
            --bg-color: #f8f9fa;
            --card-bg: #ffffff;
            --text-color: #212529;
        }
 
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 0;
        }
 
        header {
            background-color: var(--primary-color);
            color: white;
            padding: 1rem 2rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
 
        header h1 { margin: 0; font-size: 1.5rem; }
 
        main {
            max-width: 900px;
            margin: 30px auto;
            padding: 20px;
            background: var(--card-bg);
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }
 
        .alerta {
            background-color: #f8d7da;
            color: #842029;
            border: 1px solid #f5c2c7;
            padding: 12px;
            border-radius: 6px;
            margin-bottom: 20px;
        }
 
        footer {
            text-align: center;
            padding: 20px;
            font-size: 0.85rem;
            color: #6c757d;
        }
    </style>
</head>
<body>
 
    <header>
        <h1>⚡ Painel de Controle - Gestão de Clientes</h1>
    </header>
 
    <main>
        <!-- Injeção dinâmica das páginas filhas -->
        {{!base}}
    </main>
 
    <footer>
        <p>Desenvolvido com Python 3, Bottle e SQLite</p>
    </footer>
 
</body>
</html>