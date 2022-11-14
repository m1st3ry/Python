import math

tamanho = float(input("Informe o tamanho em metros quadrados a ser pintado: "))

lt18 = 18
val18 = 80

lt36 = 3.6
val36 = 25
# quantidade de metros quadrados por litro
qtidade_litros = tamanho / 6

# calculo de valor e quantidade de latas de 18 litros
qtidade_latas = math.ceil(qtidade_litros / lt18)
custo_lt = qtidade_latas * val18
print("Quantidade em latas de 18 litrs: ")
print(f"O cliente necessita comprar {qtidade_latas} latas, que sai ao custo de R$ {custo_lt} reais.")

# calculo de valor e quantidade de garrafas de 3,6
qtidade_garrafa = math.ceil(qtidade_litros / lt36)
custo_garrafa = qtidade_garrafa * val36
print("Garrafas de 3,6 litros:")
print(f"O cliente necessita comprar {qtidade_garrafa}, no custo de R$ {custo_garrafa} reais.")

# usar garrafas e latas afim de cortar o desperdicio financeiro e aumentar 10% por segurança
lfolga = qtidade_litros * 1.1
qlatasX = lfolga // lt18

lfolga_falta =  lfolga  - (qlatasX * lt18)
qgarrafasX = math.ceil(lfolga_falta / lt36)

valor_real = (qlatasX * val18) + (qgarrafasX * val36)

print(f"O cliente necessita comprar {qlatasX} latas e {qgarrafasX} garrafas, ao custo de R${valor_real} reais.")