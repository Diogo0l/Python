import tkinter as tk
import tkinter.messagebox

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
        print(
            f"RG: {rg},",
            f"Nome: {aluno['nome']},",
            f"Sexo: {aluno['sexo']},",
            f"Endereço: {aluno['endereco']},",
            f"Data de Nascimento: {aluno['datanasc']}\n",
        )


"""while True:
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
            break"""
        
janela = tk.Tk()
janela.title("Cadastro de Alunos")
janela.configure(bg="lightblue")

label_principal = tk.Label(janela, text="Cadastro de Alunos", font=("Arial", 16)).pack(pady=10, padx=10)
label_nome = tk.Label(janela, text="Nome:", font=("Arial", 12)).pack(pady=5, padx=10)
entry_nome = tk.Entry(janela, font=("Arial", 12))
entry_nome.pack(pady=5, padx=10)

label_sexo = tk.Label(janela, text="Sexo:", font=("Arial", 12)).pack(pady=5, padx=10)
entry_sexo = tk.Entry(janela, font=("Arial", 12))
entry_sexo.pack(pady=5, padx=10)

label_endereco = tk.Label(janela, text="Endereço:", font=("Arial", 12)).pack(pady=5, padx=10)
entry_endereco = tk.Entry(janela, font=("Arial", 12))
entry_endereco.pack(pady=5, padx=10)

label_datanasc = tk.Label(janela, text="Data de Nascimento:", font=("Arial", 12)).pack(pady=5, padx=10)
entry_datanasc = tk.Entry(janela, font=("Arial", 12))
entry_datanasc.pack(pady=5, padx=10)

label_rg = tk.Label(janela, text="RG:", font=("Arial", 12)).pack(pady=5, padx=10)
entry_rg = tk.Entry(janela, font=("Arial", 12))
entry_rg.pack(pady=5, padx=10)

botao_cadastrar = tk.Button(janela, text="Cadastrar", font=("Arial", 12), command=lambda: cadastrar_aluno(entry_nome.get(), entry_sexo.get(), entry_endereco.get(), entry_datanasc.get(), entry_rg.get())).pack(pady=10, padx=10)

def cadastrar_aluno(nome, sexo, endereco, datanasc, rg):
    if verificar_rg(rg):
        tk.messagebox.showerror("Erro", "RG já cadastrado. Tente novamente.")
        return

    aluno = {
        "nome": nome,
        "sexo": sexo,
        "endereco": endereco,
        "datanasc": datanasc,
        "rg": rg,
    }
    alunos[rg] = aluno
    tk.messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
      

label_mostrar_alunos = tk.Label(janela, text="Alunos cadastrados:", font=("Arial", 12)).pack(pady=5, padx=10)
text_alunos = tk.Label(janela, height=5, width=100, font=("Arial", 12))
text_alunos.pack(pady=5, padx=10)

botao_mostrar_alunos = tk.Button(janela, text="Mostrar Alunos", font=("Arial", 12), command=lambda: text_alunos.config(text=str(alunos)))
botao_mostrar_alunos.pack(pady=10, padx=10)  


janela.mainloop()