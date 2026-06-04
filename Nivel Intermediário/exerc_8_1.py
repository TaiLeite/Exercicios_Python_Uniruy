'''Exercício 8: Dicionário de Contatos
Crie um programa que gerencie uma lista de contatos. Cada contato deve ter nome, telefone e
e-mail, armazenados em um dicionário. Permita adicionar, buscar e listar contatos.'''      


contato = {} #Dicionário para armazenar os contatos, onde a chave é o nome do contato e o valor é outro dicionário contendo o telefone e email do contato

def adicionar (): # Função para adicionar um novo contato ao dicionário de contatos
    print("\n---Adicionar contato a lista---")
    nome = input("Digite o nome: ").strip() #Solicita ao usuário o nome do contato e remove espaços em branco extras
    telefone = input("Digite o numero do telefone: ")
    email = input("Digite o email: ")
    contato[nome] = {"telefone": telefone, "email": email} #Adiciona o contato ao dicionário, onde a chave é o nome do contato e o valor é outro dicionário contendo o telefone e email do contato
    print ("Contato adicionado com sucesso!")

def buscar ():# Função para buscar um contato no dicionário de contatos e exibir suas informações
    print("\n---Buscar contatos---")
    nome = input("Digite o nome do contato: ").strip() #Solicita ao usuário o nome do contato e remove espaços em branco extras
    if nome in contato: #Verifica se o nome do contato existe no dicionário e exibe as informações do contato
        print(f"Nome: {nome}")
        print(f"Telefone: {contato[nome]['telefone']}") #Acessa o número de telefone do contato usando a chave 'telefone' no dicionário do contato
        print(f"Email: {contato[nome]['email']}" ) #Acessa o email do contato usando a chave 'email' no dicionário do contato
    else: print("Contato nao encontrado")

def listar():
    if not contato: #Verifica se o dicionário de contatos está vazio e exibe uma mensagem caso não haja contatos cadastrados
        print("A lista esta vazia")
    
    else:
        print("\n---Lista de contatos---")
        for nome, info in contato.items(): #Loop para iterar sobre os contatos no dicionário e exibir as informações de cada contato, onde nome é a chave do contato e info é o valor do contato (outro dicionário contendo telefone e email)
            print(f"Nome: {nome}")
            print(f"Telefone: {info['telefone']}")
            print(f"Email: {info['email']}")

def remover():
    nome = input("Digite o nome do contato: ").strip()
    if nome in contato:
        del contato[nome]
        print("Contato removido")

def menu ():
    while True: #Loop para exibir o menu de opções e solicitar a escolha do usuário até que ele decida sair do programa
        print("-" *30)
        print("Lista de contatos: ")
        print("1. Adicionar novos contatos: ")
        print("2. Buscar contatos: ")
        print("3. Listar contatos: ")
        print("4. Remover contato: ")
        print("5. Sair da lista de contatos." )
        print("-" * 30)
        opcao = (input("Digite uma opcao: "))

        match opcao:
            case '1':
                adicionar ()
            case '2':
                buscar()
            case '3':
                listar()
            case '4':
                remover()
            case '5':
                print("Sair da lista")
                break #Encerra o loop e sai do programa quando o usuário escolhe a opção 5
            case _:#Caso o usuário digite uma opção inválida, exibe uma mensagem de erro
                print("Opcao invalida")

if __name__ == "__main__":
    menu()