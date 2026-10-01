alunos = {}
aluno = {}

def mostrar_menu():
    print("Cadastro de Alunos")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    return opcao

def receber_dados():
    nome = input("Digite o nome do aluno: ")
    sexo = input("Digite o sexo do aluno: ")
    endereco = input("Digite o endereço do aluno: ")
    datanasc = input("Digite a data de nascimento do aluno (dd/mm/aaaa): ")
    rg = input("Digite o RG do aluno: ")
        
    aluno = {
        "nome": nome,
        "sexo": sexo,
        "endereco": endereco,
        "datanasc": datanasc,
        "rg": rg
    }
    alunos[rg] = aluno
    print("Aluno cadastrado com sucesso!\n")
    return aluno, rg

while True:
    opcao = mostrar_menu()

    match opcao:
        case "1":
            aluno, rg = receber_dados()
            alunos[rg] = aluno
            print("Aluno cadastrado com sucesso!")

   