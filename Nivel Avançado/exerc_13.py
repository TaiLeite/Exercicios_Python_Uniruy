'''Exercício 13: Registro de Logs
Escreva um programa que registre mensagens de log em um arquivo. As mensagens devem
incluir um timestamp e o tipo de log (INFO, WARNING, ERROR). Utilize o módulo datetime.'''

import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, filename='logfile.log', format='%(asctime)s - %(levelname)s - %(message)s')

def registrar_log (tipo, mensagem, nome_arquivo="sistema.log"):
          
    # Formata data atual no padrão: di/Mês/ano Hora:Minuto:Segundo
    data_formatada= datetime.now().strftime("%d/%m/%y %H:%M:%S")
    
    # Monta a linha do log padronizada
    linha_log = (f"[{data_formatada}] [{tipo.upper()}] - {mensagem}\n")
    
    try:
        # Abre o arquivo no modo 'a' (append), que adiciona o texto ao final do arquivo sem apagar o que já existe
        with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
            arquivo.write(linha_log)
            logging.info(f"Log de {tipo} registrado com sucesso!")
            
    except Exception as erro:
        print(f"Erro ao tentar gravar no arquivo de log: {erro}")

# --- Demonstração de Uso ---
# Simulando diferentes eventos no sistema

registrar_log("INFO", "O sistema foi iniciado com sucesso.")
registrar_log("WARNING", "O uso de memória RAM ultrapassou 80%.")
registrar_log("ERROR", "Falha ao conectar com o banco de dados.")
