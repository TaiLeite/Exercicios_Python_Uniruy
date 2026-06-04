'''Calculadora Simples
Desenvolva uma calculadora que peça dois números ao usuário e, em seguida, exiba a soma,
subtração, multiplicação e divisão entre eles.'''

def subtracao():
    num1 =  float(input("Digite um numero: "))
    num2 = float(input("Digite o segundo numero: "))
    resultado = num1 - num2
    print(f"A subtração de {num1} e {num2} eh igal a {resultado}")

def soma():
    num1 = float(input("Digite um numero: "))
    num2 = float(input("Digite o segundo numero: "))
    resultado = num1 + num2
    print (f"A soma de {num1} e {num2} eh igual a {resultado}")

def multiplicacao():
    num1 = float(input("Digite um  numero: "))
    num2  = float(input("Digite o segundo numero: "))
    resultado = num1 * num2
    print(f" A multiplicacao entre o {num1} e {num2} eh igual a {resultado}")
                                      
def divisao():
    num1 = float(input("Digite um numero: "))
    num2 = float(input("Digite o segundo numero: "))
    resultado = num1/num2
    print(f"A divisao entre o {num1} e {num2} eh igual a {resultado}")  

def menu():
    while True:
        
        print("1 - Soma")
        print("2 - Subtracao")
        print("3 - Multiplicacao")
        print("4 - Divisao")
        print("5 - Sair da calculadora")

        opcao = input("Digite uma opcao: ")

        match opcao:
            case '1':
                soma()
            case '2':
                subtracao()
            case '3':
                multiplicacao()
            case'4':
                divisao()
            case'5':
                print("saindo da calculatdora")
                break
            case _:
                print("Opcao invalida")

if __name__ == "__main__":
    menu()