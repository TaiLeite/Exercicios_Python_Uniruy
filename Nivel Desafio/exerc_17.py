'''Exercício 17: Sistema Bancário (POO)
Crie um sistema bancário simples utilizando Programação Orientada a Objetos. Crie classes como ContaBancaria, Cliente e Banco.
A classe ContaBancaria deve ter atributos como numero_conta, saldo e titular. Métodos para depositar, sacar e verificar_saldo.
A classe Cliente deve ter nome, cpf e uma lista de ContasBancarias.
A classe Banco deve gerenciar uma lista de Clientes e permitir adicionar novos clientes e buscar contas'''


class ContaBancaria: # Classe que representa uma conta bancária, com atributos para número da conta, saldo e titular, e métodos para operações bancárias
    def __init__(self, numero_conta, titular):
        self.numero_conta = numero_conta # O número da conta é um identificador único para cada conta bancária
        self.saldo = 0.0
        self.titular = titular # O titular é um objeto da classe Cliente, representando o cliente que possui a conta

    def depositar(self, valor):# O método depositar permite adicionar um valor ao saldo da conta, desde que o valor seja positivo
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):# O método sacar permite retirar um valor do saldo da conta, desde que o valor seja positivo e haja saldo suficiente para a operação 

        if valor > 0: # Verifica se o valor do saque é positivo
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Valor de saque deve ser positivo.")

    def verificar_saldo(self): # O método verificar_saldo exibe o saldo atual da conta bancária
        print(f"Saldo atual da conta {self.numero_conta}: R${self.saldo:.2f}")

class Cliente: # Classe que representa um cliente do banco, com atributos para nome, CPF e uma lista de contas bancárias, e um método para adicionar contas
    def __init__(self, nome, cpf): # O construtor da classe Cliente recebe o nome e o CPF do cliente e inicializa uma lista vazia para armazenar as contas bancárias associadas a esse cliente

        self.nome = nome
        self.cpf = cpf
        self.contas = [] # Atributo que armazena as contas bancárias associadas ao cliente

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        print(f"Conta {conta.numero_conta} adicionada para o cliente {self.nome}.")

class Banco: # Classe que representa o banco, com um atributo para armazenar a lista de clientes e métodos para adicionar clientes e buscar contas bancárias

    def __init__(self):# O construtor da classe Banco inicializa uma lista vazia para armazenar os clientes do banco
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nome} adicionado ao banco.")

    def buscar_conta(self, numero_conta): # O método buscar_conta percorre a lista de clientes e suas respectivas contas bancárias para encontrar uma conta com o número de conta especificado. Se a conta for encontrada, ela é retornada; caso contrário, uma mensagem de erro é exibida e None é retornado.

        for cliente in self.clientes:
            for conta in cliente.contas:
                if conta.numero_conta == numero_conta:
                    return conta
        print("Conta não encontrada.")
        return None # Retorna None se a conta não for encontrada
    