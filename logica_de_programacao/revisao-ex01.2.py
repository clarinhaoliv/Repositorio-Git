#Usando importação
from datetime import datetime

# Solicita o nome e a idade do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Obtém o ano atual
ano_atual = datetime.now().year

# Calcula o ano em que a pessoa completará 100 anos
ano_cem = ano_atual + (100 - idade)

# Imprime a mensagem personalizada
print(f"{nome}, você completará 100 anos no ano de {ano_cem}.")