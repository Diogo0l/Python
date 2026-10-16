<!-- botao.tpl alternativo (com efeito de mouse) -->
<style>
    .btn-com-hover {
        display: inline-block; 
        padding: 10px 20px; 
        background-color: #007bff; 
        color: #ffffff; 
        text-decoration: none; 
        border-radius: 5px; 
        font-family: sans-serif; 
        font-weight: bold;
        transition: background-color 0.2s;
    }
    .btn-com-hover:hover {
        background-color: #0056b3; /* Cor muda ao passar o mouse */
    }
</style>

<a href="{{url_rota}}">
<button type="button" class="btn-com-hover">
    {{texto_botao}}
</button>
</a>