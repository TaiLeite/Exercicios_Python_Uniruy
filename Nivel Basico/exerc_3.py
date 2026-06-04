'''Verificador de Par ou Ímpar
Escreva um programa que receba um número inteiro e determine se ele é par ou ímpar.'''

num = int(input("Digite um numero: "))

if num % 2 == 0:
    print(f" O numnero {num} eh par")
else: print(f" O nummero {num} eh impar")

