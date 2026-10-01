alunos = {}
aluno = {}

while True:
    print("Cadastro de Alunos")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
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

    elif opcao == "2":
        if not alunos:
            print("Nenhum aluno cadastrado.\n")
        else:
            print("Lista de Alunos:")
            for rg, aluno in alunos.items():
                print(f"Nome: {aluno['nome']}, Sexo: {aluno['sexo']}, RG: {aluno['rg']}")
            print()

    elif opcao == "3":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.\n")