#criar um sistema de condomínio para organizar a entrada de visitantes e moradores, atraves do defaultdict
# O sistema deve permitir cadastrar moradores e visitantes, e organizar as informações de acordo com a categoria (morador ou visitante). O defaultdict será utilizado para facilitar a organização dos dados, evitando erros ao tentar acessar chaves que ainda não existem no dicionário.
from collections import defaultdict

condominio = defaultdict(list)

def cadastro_morador():
    nome = input("---Digite o nome do morador: ").strip()   
    apartamento = int(input("Digite o numero do apartamento: "))
    condominio['morador'].append({'nome': nome, 'apartamento': apartamento})

    print("Morador cadastrado com sucesso!")

def cadastro_visitante():
    nome = input("--- Digite o nome do visitante: ").strip()
    apartamento = input("---Digite o numero do apartamento: ")
    dt_visita = input("Digite a data da visita: DD/MM/AAAA: ")
    condominio['visitante'].append({'nome': nome, 'apartamento': apartamento, 'data_da_visita': dt_visita})
    print("Visitante cadastrado com sucesso!")

def lista_visitantes():
    if not condominio['visitante']:
        print("Nenhum visitante cadastrado.")
    else:
        print("\n---Lista de visitantes---")
        for visitante in condominio['visitante']:
            print(f"Nome: {visitante['nome']}")
            print(f"Apartamento: {visitante['apartamento']}")
            print(f"Data da visita: {visitante['data_da_visita']}")
            print("-"*30)

def menu():
    while True:
        
        print('-'*20)
        print("1 - Morador")
        print("2 - Visitante")
        print("3 - Listar visitantes ")
        print("4 - Sair do Sistema ")
        print('-'*20)
        opcao = input("Digite uma opção: ")
        
        match opcao:
            case '1':
                cadastro_morador()
            case'2':
                cadastro_visitante()
            case'3':
                lista_visitantes()
                
            case '4':
                print("Saindo do sistema. Tenha um bom dia!")
                break
            case _:
                print("Opção invalida")
        
if __name__ == "__main__":
    menu()     
        
    
    
                                  
                                  