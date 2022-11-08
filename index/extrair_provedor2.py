email = "robinson.vatam@gmail.com"
usuario, dominio = email.split("@")

print(usuario)
print(dominio)
# aqui separamos usuario de dominio

indice_ponto = dominio.index(".")
provedor = dominio[0:indice_ponto]

print("O usuário é: ", usuario)
print("O provedor é: ", provedor)