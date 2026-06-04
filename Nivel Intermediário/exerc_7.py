#Exercício 7: Contador de Vogais
#Escreva uma função que receba uma string como parâmetro e retorne o número de vogais (a,e, i, o, u) presentes nela.

def contador_vogais():#Função para contar o número de vogais em uma palavra fornecida pelo usuário
    
    palavra = input("Digite uma palavra: ").upper()

    vogais = "" #Variável para armazenar as vogais encontradas na palavra

    for letra in palavra: #Loop para iterar sobre cada letra da palavra e verificar se é uma vogal
        if letra in "AEIOU":
            vogais += letra
            
    print ("vogais: ", vogais)
    print ("Quantidade de vogais: ", len(vogais))
    
if __name__ == "__main__":
    contador_vogais()