'''Exercício 12: Gerador de Senhas
Desenvolva um gerador de senhas aleatórias. A senha deve ter um comprimento definido pelo
usuário e pode incluir letras maiúsculas, minúsculas, números e caracteres especiais. Utilize o
módulo random'''

import random
import string   

comprimento = 0
caracteres = string.ascii_letters + string.digits + string.punctuation #Define os caracteres que podem ser usados na senha
senha = []

print("Bem-vindo ao Gerador de Senhas!")
comprimento = int(input("Digite o comprimento da senha desejada: ")) #Solicita ao usuário o comprimento da senha

for i in range(comprimento):
    senha.append(random.choice(caracteres)) #Adiciona um caractere aleatório à senha
    senha_final = ''.join(senha) #Converte a lista de caracteres em uma string

print (f"Sua senha gerada e: '{senha_final}'") #Exibe a senha gerada para o usuário

