'''Exercício 15: Análise de Dados Simples (CSV)
Utilize o módulo csv para ler um arquivo CSV contendo dados de vendas (ex: produto,
quantidade, preço). Calcule o total de vendas e o produto mais vendido.'''

import csv


# Criando um arquivo CSV de exemplo para teste
dados_exemplo = [
    ['produto', 'quantidade', 'preco'],
    ['Notebook', '5', '3500.00'],
    ['Mouse Sem Fio', '20', '80.00'],
    ['Teclado Mecânico', '12', '250.00'],
    ['Monitor 24"', '8', '900.00'],
    ['Mouse Sem Fio', '15', '80.00']
]

nome_arquivo = 'vendas.csv'# Nome do arquivo CSV onde os dados de vendas serão armazenados

#  Escrevendo os dados no arquivo CSV
with open(nome_arquivo, mode='w', encoding='utf-8', newline='') as arquivo: 
    escritor_csv = csv.writer(arquivo) # Criando um objeto escritor para escrever no arquivo CSV
    escritor_csv.writerows(dados_exemplo) # Escreve as linhas de dados no arquivo CSV

def analisar_vendas(vendas_csv):
    total_vendas = 0
    vendas_por_produto = {}

    try:
        with open(vendas_csv, mode='r', encoding='utf-8') as arquivo:
            leitor_csv = csv.DictReader(arquivo) # Criando um objeto leitor para ler o arquivo CSV como dicionário
            for linha in leitor_csv:
                produto = linha['produto']
                quantidade = int(linha['quantidade'])
                preco = float(linha['preco'])
                
                total_vendas += quantidade * preco # Calculando o total de vendas acumulando o valor de cada linha (quantidade * preço)
                
                if produto in vendas_por_produto: # Verificando se o produto já está no dicionário de vendas por produto
                    vendas_por_produto[produto] += quantidade
                else:
                    vendas_por_produto[produto] = quantidade

        produto_mais_vendido = max(vendas_por_produto, key=vendas_por_produto.get) # Encontrando o produto com a maior quantidade vendida
        
        print(f"Total de Vendas: R${total_vendas:.2f}")
        print(f"Produto Mais Vendido: {produto_mais_vendido} (Quantidade: {vendas_por_produto[produto_mais_vendido]})")

    except FileNotFoundError: # Tratando o erro caso o arquivo CSV não seja encontrado
        print(f"Arquivo '{vendas_csv}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


analisar_vendas(vendas_csv=nome_arquivo)