import math

tamanho = float(input("Informe o tamanho em metros quadrados a ser pintado: "))

lt18 = 18
val18 = 80

lt36 = 3.6
val36 = 25

qtidade_litros = tamanho / 6

qtidade_latas = math.ceil(qtidade_litros / lt18)
custo_lt = qtidade_latas * val18
print("Quantidade em latas de 18 litrs: ")
print(f"O cliente necessita comprar {qtidade_latas} latas, que sai ao custo de R$ {custo_lt}.")

qtidade_garrafa = math.ceil(qtidade_litros / lt36)
custo_garrafa = qtidade_garrafa * val36
print("Garrafas de 3,6 litros:")
print(f"O cliente necessita comprar {qtidade_garrafa}, no custo de R$ {custo_garrafa}.")