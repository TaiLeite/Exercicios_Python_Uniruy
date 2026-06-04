'''Exercício 20: Jogo da Forca (POO)
Implemente o jogo da forca utilizando conceitos de Programação Orientada a Objetos. Crie classes para Jogo, Palavra e Jogador. O jogo deve permitir ao jogador adivinhar letras, exibir o estado atual da palavra e controlar o número de tentativas.'''

import random
class Palavra: # Classe que representa a palavra a ser adivinhada no jogo da forca, com um atributo para armazenar a palavra e um método para verificar se uma letra está presente na palavra
    def __init__(self, palavra):
        self.palavra = palavra.lower() # A palavra é convertida para minúsculas para facilitar a comparação

    def verificar_letra(self, letra): # O método verificar_letra recebe uma letra como argumento e retorna True se a letra estiver presente na palavra, ou False caso contrário
        return letra.lower() in self.palavra
    
class Jogador: # Classe que representa o jogador do jogo da forca, com um atributo para armazenar o nome do jogador e um método para fazer uma tentativa de adivinhação
    def __init__(self, nome):
        self.nome = nome

    def tentar_adivinhar(self, letra): # O método tentar_adivinhar recebe uma letra como argumento e retorna a letra em minúsculas para garantir consistência na comparação
        return letra.lower()    
    
class Jogo: # Classe que representa o jogo da forca, com atributos para armazenar a palavra a ser adivinhada, o jogador, o número de tentativas restantes e as letras adivinhadas, e métodos para iniciar o jogo, exibir o estado atual da palavra e processar as tentativas do jogador     

    def __init__(self, palavra, jogador):
        self.palavra = Palavra(palavra) # A palavra a ser adivinhada é representada por um objeto da classe Palavra
        self.jogador = Jogador(jogador) # O jogador do jogo é representado por um objeto da classe Jogador
        self.tentativas_restantes = 6 # O número de tentativas restantes é inicializado com um valor padrão (6)
        self.letras_adivinhadas = set() # Um conjunto para armazenar as letras que já foram adivinhadas pelo jogador

    def exibir_estado_atual(self): # O método exibir_estado_atual exibe o estado atual da palavra, mostrando as letras adivinhadas e os espaços para as letras ainda não adivinhadas
        estado = ''.join([letra if letra in self.letras_adivinhadas else '_' for letra in self.palavra.palavra])
        print(f"Palavra: {estado}")
        print(f"Tentativas restantes: {self.tentativas_restantes}")

    def processar_tentativa(self, letra): # O método processar_tentativa recebe uma letra como argumento e verifica se a letra está presente na palavra. Se estiver presente, a letra é adicionada ao conjunto de letras adivinhadas; caso contrário, o número de tentativas restantes é decrementado
        if self.palavra.verificar_letra(letra):
            self.letras_adivinhadas.add(letra)
            print("Letra correta!")
        else:
            self.tentativas_restantes -= 1
            print("Letra incorreta!")

    def iniciar_jogo(self): # O método iniciar_jogo inicia o jogo da forca, permitindo que o jogador faça tentativas até que ele adivinhe a palavra ou fique sem tentativas restantes
        print(f"Bem-vindo ao Jogo da Forca, {self.jogador.nome}!")
        while self.tentativas_restantes > 0:
            self.exibir_estado_atual()
            letra = input("Digite uma letra para adivinhar: ")
            self.processar_tentativa(letra)

            if all(letra in self.letras_adivinhadas for letra in self.palavra.palavra):
                print(f"Parabéns, {self.jogador.nome}! Você adivinhou a palavra '{self.palavra.palavra}'!")
                break   
        else:
            print(f"Game Over! A palavra era '{self.palavra.palavra}'.")        

if __name__ == "__main__":
    palavras_possiveis = ['python', 'programacao', 'desenvolvimento', 'jogo', 'forca'] # Lista de palavras possíveis para o jogo da forca
    palavra_escolhida = random.choice(palavras_possiveis) # Seleciona aleatoriamente uma palavra da lista de palavras possíveis
    nome_jogador = input("Digite o nome do jogador: ") # Solicita ao usuário o nome do jogador
    jogo = Jogo(palavra_escolhida, nome_jogador) # Cria uma instância do jogo da forca com a palavra escolhida e o nome do jogador
    jogo.iniciar_jogo() # Inicia o jogo da forca