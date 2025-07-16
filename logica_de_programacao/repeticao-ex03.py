'''Desenvolva um programa em python que ultilize WHILE para permitir
o cadastro de um número indeterminado de funcionários.O programa deve
encerrar o cadastro quando o usuário digitar 0 e,ao final, exibir a
lista completa ds funcionários registrados'''

funcionarios = []

while True:
    nome = input("Digite o nome do funcionário (ou 0 para encerrar): ")

    if nome == "0":
        break  # Encerra o loop se o usuário digitar 0

    #impedir que o usuário envie um campo vazio de funcionários

    if nome.strip() == "": #strip(): remove espaços em branco
        print("O nome do funcionário não pode ser vazio. Tente novamente.")
        continue 

    funcionarios.append(nome)  # Adiciona o nome à lista

print("\n Lista de funcionários cadastrados: ")

for i, funcionario in enumerate(funcionarios, 1): #enumerate: itera sobre a sequência
#itera = repetir
#enumerate(objeto a ser percorrido, valor inicial do índice)
        print(f"{i}. {funcionario}")

