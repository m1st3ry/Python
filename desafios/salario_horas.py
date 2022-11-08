salario = float(input("Informe o salario: "))
# sálario em carteira.
extra = float(input("Informe as horas extras: "))
# hora extra, aceito em decimais utilizando ponto no lugar da virgula.
falta = int(input("Informe a quantidade de falta: "))
# falta marcada em dias, valor em número inteiro.

dsr = 55.46
salario_h = salario / 220
# valor da hora de trabalho, divido por 220 horas mensais, previsto em lei.
desc_falta = (salario_h * 11) * falta
# valor do dia de falta, baseado em 11 horas de trabalho por dia.

hora_extra = extra * ((salario_h * 0.5 ) + salario_h)
# valor da hora extra, acrescido de 50%
adicional = (0.20 * salario_h) * 105
# adicional noturno, acrescido de 20% das 22 as 5 por dia, aqui multiplicado por 15 dias mensais.
salario_total = ((salario + hora_extra) + adicional) + dsr
# calculo do salário bruto.

if salario_total <= 1700:
    desconto = 7.8
    # aliquota inss mais baixa.
elif salario_total <= 2000:
    desconto = 8
    # aliquota inss media.
else:
    desconto = 8.7
    # aliquota inss mais alta.

inss = salario_total * (desconto / 100) 
# valor do desconto de inss.

vale = 31.09
# valor do vale diario.
vale_extra = (31.09 / 11) * extra
# valor do vale por hora, baseado em 11 horas por dia.
vale_total = 682 + vale_extra
# valor do vale total, acrescido do vale por hora.
if falta > 0:
    vale_falta = (31.09 * 7) + (31.09 * falta)
else:
    vale_falta = 0
# se houver falta, incluir (31*7)
# desconto sobre o vale quando há faltas.
vale_final = vale_total - vale_falta
# valor final, acrescido de extra e/ou faltas.


desconto_vale = (vale_final * 0.22) - vale_falta
# calculo do desconto de 20% sobre o vale total menos o valor referente a falta, valor usado para desconto no salario bruto.

liquido_s = ((salario_total - inss ) - desc_falta) - desconto_vale
# calculo final do salario liquido.

print("************************************************************************************************")
print("Seu salario bruto é de %.2f, seu desconto do inss é %.2f e seu salario liquido é de %.2f. " % (salario_total, inss, liquido_s ))
print("************************************************************************************************")
print("Seu vale refeição é de %.2f, e o desconto do vale refeição é de %.2f" % (vale_final, desconto_vale))
print("************************************************************************************************")
print("Seu adicional noturno foi de %.2f e suas horas extras em reais foi de R$ %.2f e sua falta custou R$ %.2f" % (adicional, hora_extra ,desc_falta))
print("************************************************************************************************")