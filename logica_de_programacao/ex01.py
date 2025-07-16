'''Faça um programa que leia um nome de usuário e a sua senha e não 
aceite a senha igual ao nome do usuário, mostrando uma mensagem de 
erro e voltando a pedir as informações'''

while True:
    nome_usuario = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")

    if senha.lower == nome_usuario.lower():
        print("Erro: A senha não pode ser igual ao nome do usuário. Tente novamente.\n")
    else:
        break

print("Cadastro realizado com sucesso!")