'''Exercício 9: Fatorial de um Número
Desenvolva uma função recursiva para calcular o fatorial de um número inteiro positivo.'''

def fatorial(n): #Função recursiva para calcular o fatorial de um número inteiro positivo
    if n == 0 or n == 1: #Caso base: o fatorial de 0 ou 1 é igual a 1
        return 1
    else:
        return n * fatorial(n - 1) #Chamada recursiva para calcular o fatorial de n, multiplicando n pelo fatorial de n-1       
num = int(input("Digite um numero inteiro positivo: ")) #Solicita ao usuário um número inteiro positivo para calcular o fatorial
if num < 0: #Verifica se o número é negativo e exibe uma mensagem de erro caso seja
    print("Erro: O numero deve ser inteiro positivo.")
else:
    resultado = fatorial(num)
    print(f"O fatorial de {num} é {resultado}.")    

