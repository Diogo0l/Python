alunos = {}
aluno = {}


def mostrar_menu():  # Função que mostra o menu de opções
    print("Cadastro de Alunos")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")
    return opcao

def receber_dados():  # Função que recebe os dados do aluno
    
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
        "rg": rg,
    }
    alunos[rg] = aluno
    return aluno, rg

def verificar_rg(rg):  # Função que verifica se o RG já está cadastrado
    if rg in alunos:  # noqa: SIM103
        return True
    return False

def mostrar_alunos(alunos):  # Função que mostra os alunos cadastrados
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
        return

    print("Alunos cadastrados:")
    for rg, aluno in alunos.items():
        print(f"RG: {rg},", f"Nome: {aluno['nome']},", f"Sexo: {aluno['sexo']},", f"Endereço: {aluno['endereco']},", f"Data de Nascimento: {aluno['datanasc']}\n")


while True:
    opcao = mostrar_menu()

    match opcao:
        case "1":
            aluno, rg = receber_dados()
            if not verificar_rg(rg):
                print("RG já cadastrado. Tente novamente.\n")
                continue
            alunos[rg] = aluno
            print("Aluno cadastrado com sucesso!")
            
        case "2":
           mostrar_alunos(alunos)
           
        case "3":
            print("Saindo do programa...")
            break
