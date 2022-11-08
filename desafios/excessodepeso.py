peso_peixe = float(input("Informe o peso do peixe: "))

if peso_peixe > 50:
    excesso = peso_peixe - 50
    print('O excesso de peixe foi de: ',excesso)
else:
    excesso = 0
    
    
multa = excesso * 4

print('O peso de peixe foi de ', peso_peixe, ' quilos')
print(f'A multa pelo excesso foi de R${excesso:,.2f}')    
