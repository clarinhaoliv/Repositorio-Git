#Função X Classe
#Função: bloco de códigos que executa uma tarefa
#Classe: modelo para criar objetos
#Objeto: estrutura que representa uma unidade do mundo real ou conceito abstrato dentro de um programa

class ContaBancaria:
    def __init__(self , titular , saldo_inicial=0):
#Quando utilizar _init_: quando precisa inicializar o objeto com algum valor ou configuração
        self.titular = titular # intância atual do objeto
        self.saldo = saldo_inicial

    def depositar(self , valor):
        if valor > 0:
            self.saldo += valor #self.saldo =self.saldo + valor
            print(f"Depósito de R${valor:.2f}")
        else:
            print("Valor de depósito inválido!")
    
#criar funções sacar e consultar_saldo

    def sacar(self, valor):
        if valor < 0:
            print("Valor de saque inválido!")
        elif valor > self.saldo:
            print("Saldo insuficiente para saque.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def consultar_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")
        
conta = ContaBancaria("José", 1000)
conta.consultar_saldo()
conta.depositar(700)
conta.sacar(200)
conta.consultar_saldo()

        



