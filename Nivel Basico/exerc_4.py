'''Exercício 4: Tabuada
Crie um programa que solicite um número inteiro e exiba a tabuada desse número de 1 a 10.
'''
  
num = int(input("Digite um numero inteiro: ")) #Solicita ao usuario um numero inteiro para exibir a tabuada

for i in range(1,11): #Loop para iterar de 1 a 10 e calcular a tabuada do numero fornecido pelo usuario
    resultado = num * i
    
    print(f"{num} x {i}: {resultado}")
   
