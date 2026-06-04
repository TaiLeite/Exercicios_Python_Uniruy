'''Exercício 19: Web Scraper Simples
Desenvolva um pequena web scraper usando a biblioteca requests e BeautifulSoup para extrair títulos de notícias de um site de notícias (ex: G1, BBC News). Salve os títulos em um arquivo de texto.'''

# necessario instalar as bibliotecas requests e beautifulsoup4 para rodar este código

import requests
from bs4 import BeautifulSoup   

url = 'https://g1.globo.com/' # URL do site de notícias que será raspado    
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser') # Cria um objeto BeautifulSoup para analisar o conteúdo HTML da página

titles = soup.find_all('a', class_='feed-post-link') # Encontra todos os links com a classe especificada

with open('noticias.txt', 'w',  encoding='utf-8') as f: # Abre o arquivo para escrita
    for title in titles:
        f.write(title.text + '\n') # Escreve cada título em uma nova linha
print(f"{len(titles)} títulos de notícias foram salvos em 'noticias.txt'.") 
