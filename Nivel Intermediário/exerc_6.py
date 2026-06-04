#Exercício 6 - Lista de compras

#Crie um programa que permita ao usuário criar uma lista de compras. O programa deve permitir que o usuário adicione itens à lista, visualize a lista completa e remova itens da lista. O programa deve continuar a solicitar ações do usuário até que ele decida sair.

def main():
    lista = [] #
    
    while True: #Loop para continuar solicitando ações do usuário
        print('-' * 30)
        print(" Menu:")
        print("1. Adcionar itens: ")
        print("2. Visualizar lista: ")
        print("3. Remover itens:")
        print('4. Sair da lista.')
        print('-' * 30)
        opcao = input("Escolha uma opcao: ")         

        match opcao: # Estrutura de controle para executar a ação escolhida pelo usuário
            case '1':    
                item = input("Digite o item desejado: ")
                lista.append(item)
                print(" ")
                print(f"{item}, adicionado à lista.")

            case '2':
                if not lista:
                    print("Lista vazia.")
                else:
                    print('Lista de compras:')
                    for i, item in enumerate(lista,1):
                        print(f"{i}. {item}")

            case '3':
                if not lista:
                    print ("Lista vazia.")
                else: 
                    print ("Digite o item a ser removido: ")
                    item = input()
                    if item in lista:
                        lista.remove(item)
                        print(f"{item} removido da lista.")

            case '4':
                print("Sair da lista. Tenha um bom dia!")
                break
            
            case _:
                print("Opção inválida. Tente novamente.")

if __name__== "__main__": #Ponto de entrada do programa para garantir que a função main seja executada apenas quando o script for executado diretamente
    main()