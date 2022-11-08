valor_total = float(input('Digite o valor total: '))
parcela = int(input('Digite a quantidade de parcelas desejadas: '))

valor_parcela = valor_total / parcela

print("O valor da compra foi de R$ %.2f" % valor_total, " o número de parcelas informado foi ", parcela, " e o valor das parcelas é de: R$ %.2f" % valor_parcela)
