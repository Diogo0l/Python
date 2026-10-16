% rebase('base.tpl', titulo=f'Editar Cliente #{cliente}')
 
<h2>Editar Cliente</h2>
 
<form action="/editar/{{ cliente }}" method="post" style="max-width: 400px;">
    <div style="margin-bottom: 10px;">
        <label style="display:block;">Nome:</label>
        <input type="text" name="nome" value="{{ cliente }}" required style="width: 100%; padding: 8px; box-sizing: border-box;">
    </div>
 
    <div style="margin-bottom: 10px;">
        <label style="display:block;">E-mail:</label>
        <input type="email" name="email" value="{{ cliente }}" required style="width: 100%; padding: 8px; box-sizing: border-box;">
    </div>
 
    <input type="submit" value="Atualizar" style="background: var(--primary-color); color: white; border: none; padding: 10px 15px; cursor: pointer; border-radius: 4px;">
    <a href="/" style="margin-left: 10px; color: #6c757d; text-decoration: none;">Cancelar</a>
</form>