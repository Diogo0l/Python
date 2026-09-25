def cadastrar_livro(titulo, autor, disponibilidade):

    livro = {
        'titulo': titulo,
        'autor': autor,
        'disponibilidade': disponibilidade
    }

    livro_str = f"{livro['titulo']},{livro['autor']},{livro['disponibilidade']}\n"
    
    return livro_str

def listar_livros(*livros):
    livros_str = ""
    for livro in livros:
        livros_str += f"{livro['titulo']},{livro['autor']},{livro['disponibilidade']}\n"
    return livros_str

print(cadastrar_livro("007", "Machado de Assis", True))