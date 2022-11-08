ano_nascimento = int(input("Informe seu ano de nascimento: "))


idadePermitida = (2022 - ano_nascimento)

if idadePermitida >= 18:
    print("Você é de maior! Entrada liberada!")
else:
    print("Você ainda é de menor! Entrada proibida!")