'''
Contagem de vogais e consoantes 
Escreva um programa que conta o número de vogais e consoantes em uma string.

Algoritmo Checklist
- [x] Receber o texto para contar as vogais.
- [x] Percorrer o texto contando cada vogal.
- [x] Percorrer o texto contando cada consoante.
- [x] Mostrar o resultado.
'''

texto = input('Digite o texto: ')
vogais_no_texto = 0
consoantes_no_texto = 0

for caractere in texto: 
    if caractere in "aeiouAEIOU":
        vogais_no_texto += 1
        
    if caractere.lower() in "bcdfghjklmnpqrstvwxyz":
            consoantes_no_texto += 1
            
print(f"O texto {texto} tem {vogais_no_texto} vogais.")
print(f"O texto {texto} tem {consoantes_no_texto} consoantes.")