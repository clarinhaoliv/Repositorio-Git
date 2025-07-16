while True:
    nome = input("Digite seu nome: ")
    if len(nome) <= 3:
        print("Nome inválido. Deve conter mais de 3 caracteres.")
        continue

    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0 or idade > 150:
            print("Idade inválida. Deve estar entre 0 e 150.")
            continue
    except ValueError:
        print("Idade inválida. Deve ser um número inteiro.")
        continue

    try:
        salario = float(input("Digite seu salário: "))
        if salario <= 0:
            print("Salário inválido. Deve ser maior que zero.")
            continue
    except ValueError:
        print("Salário inválido. Deve ser um número.")
        continue

    print("\nInforme seu gênero:")
    print("F - Feminino")
    print("M - Masculino")
    print("O - Outros")
    genero = input("Digite seu gênero (F/M/OUTROS): ").strip().upper()
    if genero not in ['F', 'M', 'O']:
        print("Gênero inválido.")
        continue

    print("\nInforme seu estado civil:")
    print("S - Solteiro(a)")
    print("C - Casado(a)")
    print("V - Viúvo(a)")
    print("D - Divorciado(a)")
    estado_civil = input("Digite seu estado civil (S/C/V/D): ").strip().upper()
    if estado_civil not in ['S', 'C', 'V', 'D']:
        print("Estado civil inválido.")
        continue

    break

# Convertendo siglas para palavras (modo simples)
if genero == 'F':
    genero = 'Feminino'
elif genero == 'M':
    genero = 'Masculino'
else:
    genero = 'Outros'

if estado_civil == 'S':
    estado_civil = 'Solteiro(a)'

elif estado_civil == 'C':
    estado_civil = 'Casado(a)'

elif estado_civil == 'V':
    estado_civil = 'Viúvo(a)'
else:
    estado_civil = 'Divorciado(a)'

print("\nInformações registradas com sucesso:")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Salário: R${salario:.2f}")
print(f"Gênero: {genero}")
print(f"Estado Civil: {estado_civil}")