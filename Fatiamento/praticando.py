nome = "Robinson"
email = "robinson.vatam@terra.com"
cpf = "123.456.789-99"
idade = 39
salario = 1230
divida = 458.83
prova1 = 9.5
prova2 = 10
prova3 = 5
prova4 = 8.5

usuario, dominio = email.split("@")
indice_ponto = dominio.index(".")
provedor = dominio[0:indice_ponto]

dinheiro = salario - divida

media = (prova1 + prova2 + prova3 + prova4) / 4

cpf_inicial, cpf_final = cpf.split("-")
cpf1 = cpf_inicial[0:3]
cpf2 = cpf_inicial[4:7]
cpf3 = cpf_inicial[8:11]

frase1 = "O aluno %s, com cpf inicial %s e idade de %d anos, " % (nome, cpf1+cpf2+cpf3, idade)
frase2 = "recebeu %d de salário e possui uma divida de %.2f, ficando com o dinheiro de %.2f em conta." % (salario, divida, dinheiro)
frase3 = "Teve uma média de %d pontos em provas. " % media
frase4 = f"O aluno com cpf final {cpf_final} possui usuario de email {usuario} e seu provedor é o {provedor}" 


print(frase1, frase2, frase3, frase4)

