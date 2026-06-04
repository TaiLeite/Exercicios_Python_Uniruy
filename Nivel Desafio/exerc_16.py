'''Exercício 16: Análise de Dados com Pandas
Dado um arquivo CSV (ex: dados_clientes.csv com colunas Nome, Idade, Cidade, Renda):
1.Carregue os dados em um DataFrame do Pandas.
2.Calcule a média de idade e renda dos clientes.
3.Encontre a cidade com o maior número de clientes.
4.Filtre os clientes com renda acima de um valor específico.'''

import pandas as pd

dados_exemplo = {
    'Nome': ['Ana Silva', 'Bruno Costa', 'Carlos Oliveira', 'Daniela Souza', 'Eduardo Lima', 'Fernanda Alves'],
    'Idade': [28, 35, 42, 28, 50, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'São Paulo', 'Rio de Janeiro'],
    'Renda': [4500.00, 6200.00, 12000.00, 3800.00, 8500.00, 5100.00]
}
# Criando um DataFrame a partir do dicionário de dados de exemplo e salvando em um arquivo JSON para melhor visualização
pd.DataFrame(dados_exemplo).to_json('dados_clientes.json', orient='records', index=False, indent=4)

def analisar_dados(arquivo_json, renda_limite):
    try:
      
        df = pd.read_json(arquivo_json, orient='records', encoding='utf-8') # Carrega os dados do arquivo JSON para um DataFrame do Pandas

        # Calcula a média de idade e renda dos clientes
        media_idade = df['Idade'].mean()
        media_renda = df['Renda'].mean()

        # Encontra a cidade com o maior número de clientes
        cidade_mais_clientes = df['Cidade'].value_counts().idxmax()

        # Filtra os clientes com renda acima do limite especificado
        clientes_renda_alta = df[df['Renda'] > renda_limite]

        print("====== RESULTADO DA ANÁLISE ======")
        print(f"Média de Idade: {media_idade:.1f} anos")
        print(f"Média de Renda: R$ {media_renda:.2f}")
        print(f"Cidade com mais clientes: {cidade_mais_clientes}")
        print(f"\n--- Clientes com renda acima de R$ {renda_limite:.2f} ---")
        # Exibindo apenas Nome e Renda no print final para ficar mais limpo
        print(clientes_renda_alta[['Nome', 'Cidade', 'Renda']])
        print("==================================")

    except FileNotFoundError:
        print(f"Arquivo '{arquivo_json}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao analisar os dados: {e}")

if __name__ == "__main__":
    arquivo_json = 'dados_clientes.json' # Nome do arquivo JSON onde os dados dos clientes estão armazenados
    renda_limite = 5000.00 # Valor limite para filtrar os clientes com renda alta
    analisar_dados(arquivo_json, renda_limite) # Chamando a função de análise de dados com o arquivo JSON e o limite de renda especificado