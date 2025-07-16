'''Crie um programa que peça ao usuário para digitar seu nome e sua
idade. Imprima uma mensagem endereçada a ele que diga em que ano ele 
completará 100 anos'''

nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))

cem_anos = 2025 - idade
resultado = cem_anos + 100

print(f"Olá , {nome}! Você completará 100 anos no ano de {resultado}.")
