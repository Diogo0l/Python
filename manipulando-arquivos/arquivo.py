import os
from pathlib import Path

"""print(Path("primeira_pasta/segunda_pasta"))
print(type(Path("primeira_pasta/segunda_pasta"))) """

# Fazendo um loop para acessar os arquivos
"""for nome in ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt"]:
    print(Path("primeira_pasta/segunda_pasta") / nome )"""
    
'''print(Path.home)'''

'''print(Path.cwd())'''

"""p = Path('C:/Users/Aluno/Spam.txt')
print(f"Drive: {p.anchor}")
print(f"Pasta raiz do usuário do Windows: {p.parent}")
print(f"Pasta raiz do Windows: {p.drive}")
print(f"Nome do arquivo sem extensão: {p.stem}")
print(f"Extensão do arquivo: {p.suffix}")
print(f"Drive: {p.drive}")

print(f"Pasta superior: {Path.cwd().parent[0]}")
print(f"Pasta acima da superior do diretório atual: {Path.cwd().parent.parent[1]}")
print(f"Pasta superior do diretório atual: {Path.cwd().parent}")

print(list(Path.home().glob("*")))
print(list(Path.home().glob("*.txt")))"""

print(list(Path(__file__).parent.absolute().glob("*")))