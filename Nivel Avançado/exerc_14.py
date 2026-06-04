'''Exercício 14: Validador de CPF
Crie uma função que valide um número de CPF (apenas a lógica de validação, sem interface).
Pesquise o algoritmo de validação de CPF.'''

import re

def validar_cpf(cpf: str) -> bool:
    # Limpa o CPF (remove pontos, traços e espaços)
    cpf = re.sub(r'\D', '', cpf)

    #  Verifica se o CPF tem 11 dígitos ou se são todos iguais (ex: 111.111.111-11)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    #  Cálculo do Primeiro Dígito Verificador
    soma_1 = 0
    multiplicador_1 = 10
    
    for i in range(9):
        soma_1 += int(cpf[i]) * multiplicador_1
        multiplicador_1 -= 1
        
    resto_1 = soma_1 % 11
    digito_1 = 0 if resto_1 < 2 else 11 - resto_1

    #  Cálculo do Segundo Dígito Verificador
    soma_2 = 0
    multiplicador_2 = 11
    
    for i in range(10):
        soma_2 += int(cpf[i]) * multiplicador_2
        multiplicador_2 -= 1
        
    resto_2 = soma_2 % 11
    digito_2 = 0 if resto_2 < 2 else 11 - resto_2

    # Verifica se os dígitos calculados batem com os dígitos do CPF informado
    return int(cpf[9]) == digito_1 and int(cpf[10]) == digito_2

if __name__ == "__main__":

    cpf = (input("Digite um CPF para validar: "))
    print(validar_cpf(cpf))  # Deve retornar True ou False dependendo da validade do CPF
