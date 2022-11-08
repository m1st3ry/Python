salario = float(input("Informe o salario total: "))
aumento = float(input("Informe o percentual de aumento: "))

s_aumentado = salario * (aumento / 100) + salario

print("Seu salario aumentou para R$ %.2f " % s_aumentado)