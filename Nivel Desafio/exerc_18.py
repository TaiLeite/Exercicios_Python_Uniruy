'''Visualização de Dados com Matplotlib (Opcional)
Utilizando os dados do Exercício 16 (ou outros dados de sua escolha), crie um gráfico de barras da distribuição de clientes por cidade ou um histograma da distribuição de idades, usando a biblioteca matplotlib.'''



import matplotlib.pyplot as plt
import pandas as pd 

# Carregando os dados do arquivo JSON para um DataFrame do Pandas
df = pd.read_json('dados_clientes.json', orient='records', encoding='utf-8') 
# Gráfico de Barras: Distribuição de Clientes por Cidade
plt.figure(figsize=(8, 5)) # Define o tamanho da figura do gráfico      
df['Cidade'].value_counts().plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen']) # Cria um gráfico de barras usando a contagem de clientes por cidade
plt.title('Distribuição de Clientes por Cidade') # Define o título do gráfico
plt.xlabel('Cidade') # Define o rótulo do eixo X
plt.ylabel('Número de Clientes') # Define o rótulo do eixo Y
plt.xticks(rotation=45) # Rotaciona os rótulos do eixo X para melhor legibilidade
plt.tight_layout() # Ajusta o layout para evitar sobreposição de elementos
plt.show() # Exibe o gráfico
# Histograma: Distribuição de Idades dos Clientes
plt.figure(figsize=(8, 5)) # Define o tamanho da figura do gráfico  
df['Idade'].plot(kind='hist', bins=10, color='lightcoral', edgecolor='black') # Cria um histograma da distribuição de idades dos clientes
plt.title('Distribuição de Idades dos Clientes') # Define o título do gráfico
plt.xlabel('Idade') # Define o rótulo do eixo X
plt.ylabel('Frequência') # Define o rótulo do eixo Y
plt.grid(axis='y', alpha=0.75) # Adiciona uma grade horizontal para melhor visualização
plt.tight_layout() # Ajusta o layout para evitar sobreposição de elementos
plt.show() # Exibe o gráfico
