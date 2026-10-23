<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>{{ get('titulo', 'Sistema de Gestão') }}</title>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; margin: 0; background: #f8f9fa; }
        nav { background: #0d6efd; padding: 1rem 2rem; }
        nav a { color: white; text-decoration: none; margin-right: 20px; font-weight: bold; }
        nav a:hover { text-decoration: underline; }
        main { max-width: 900px; margin: 30px auto; background: white; padding: 25px; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
        .alerta { background: #f8d7da; color: #842029; padding: 10px; border-radius: 4px; margin-bottom: 15px; }
        form.card { background: #f1f3f5; padding: 15px; border-radius: 6px; margin-bottom: 25px; }
        form.card input { display: block; margin-bottom: 10px; padding: 8px; width: 100%; box-sizing: border-box; }
        form.card input[type="submit"] { background: #198754; color: white; border: none; cursor: pointer; font-weight: bold; width: auto; padding: 10px 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 15px; }
        th, td { border: 1px solid #dee2e6; padding: 10px; text-align: left; }
        th { background: #e9ecef; }
        .btn-edit { color: #0d6efd; text-decoration: none; font-weight: bold; margin-right: 10px; }
        .btn-del { color: #dc3545; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>
    <nav>
        <a href="/">👤 Clientes</a>
        <a href="/produtos">📦 Produtos</a>
    </nav>
    <main>
        {{!base}}
    </main>
</body>
</html>