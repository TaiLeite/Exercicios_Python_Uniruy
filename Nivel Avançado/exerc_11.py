'''Exercício 11: Leitor de Arquivo de Texto
Crie um programa que leia um arquivo de texto (.txt) e exiba seu conteúdo na tela. O programa
deve tratar o erro caso o arquivo não seja encontrado.'''

try:
    with open('arquivo.txt','r',encoding="utf-8") as arquivo: #Tenta abrir o arquivo 'arquivo.txt' para leitura
        conteudo = arquivo.read()#Lê o conteúdo do arquivo e armazena na variável 'conteudo'
        print(conteudo) #Exibe o conteúdo do arquivo na tela
except FileNotFoundError:   #Trata o erro caso o arquivo não seja encontrado
    print('Arquivo nao encontrado')