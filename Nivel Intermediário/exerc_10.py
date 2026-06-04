#Conversor de Temperatura
#Crie funções para converter temperaturas de Celsius para Fahrenheit e vice-versa. O programa deve perguntar ao usuário qual conversão deseja fazer e o valor da temperatura.

def celsius_farenheit(): #Função para converter Celsius para Farenheit
    celsius = float(input("Digite a temperaturda em graus Celsius: "))
    farenheit = (celsius * 1.8) + 32
    print(f"{celsius}C eh igual a {farenheit: .2f} F")


def farenheit_celsius(): #Função para converter Farenheit para Celsius
    farenheit = float(input("Digite a temperatura em graus Farenheit: "))
    celsius = (farenheit - 32)/1.8
    print(f"{farenheit}F eh igual a {celsius:.2f}C ")

   
opcao = input ("Escolha uma temperatura: 1. Celsius ou 2. Farenheit: ") #Solicita ao usuario a escolha da temperatura a ser convertida
    
match opcao:
    case '1':
        celsius_farenheit()
    case '2':
        farenheit_celsius()
    case _:
        print("Opcao invalida. Tente novamente.")

