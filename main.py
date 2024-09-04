def menu():
    opcao = input('''
                   PROJETO AGENDA EM PYTHON
    MENU:
    [1]CADASTRAR CONTATO
    [2]LISTAR CONTATO
    [3]DELETAR CONTATO
    [4]BUSCAR CONTATO
    [5]SAIR
                  
    SELECIONE UMA OPÇÃO: ''')
    
    match opcao:
        case "1":
            cadastrarContato()

        case "2":
            listarContato()

        case "3":
            deletarContato()

        case "4":
            buscarContato()
        
        case "5":
            sair()

        case _:
            print("DIGITE UMA OPÇÃO VALIDA")
            menu()
    

def cadastrarContato():
    id = input("Escolha o ID do seu contato: ")
    nome = input("Digite o nome do seu contato: ")
    telefone = input("Digite o telefone do seu contato: ")
    email = input("Digite o email do contato: ")
    try:
        agenda = open("agenda.txt", "a")
        dados = f"{id};{nome};{telefone};{email} \n"
        agenda.write(dados)
        agenda.close()
        print(f"Contato gravado com sucesso!")
    except:
        print("Erro na gravação do contato.")
    reset()


def listarContato():
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        print(contato)
    agenda.close()
    reset()

# função deletar contato não está funcionando
def deletarContato():
    nomeDeletado = input("Digite o nome para ser deletado: ").lower()
    agenda = open("agenda.txt","r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open("agenda.txt","w")
    for i in aux2:
        agenda.write(i)
    print(f"Contato deletado com sucesso!")
    listarContato()
    reset()
    

def buscarContato():
    nome = input(f"Digite o nome a ser procurado: ").upper()
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        if nome in contato.split(";")[1].upper():
            print(contato)
    agenda.close()
    reset()


def sair():
    print("Saindo da aplicação...")
    exit()


def main():
    menu()

def reset():
    voltar = input('''
VOLTAR PARA O MENU [1]
SAIR DA APLICAÇÃO [2]
''')
    if voltar == "1":
        menu()
    elif voltar == "2":
        sair()
    else:
        print("Digite uma opção valida...")
        reset()
    

main()
