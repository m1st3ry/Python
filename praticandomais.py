nome = str(input("Informe seu nome: "))
idade = int(input("Informe sua idade: "))
hora = int(input("Informe a hora de chegada sem os minutos: "))

list = ["João", "Robinson", "Marcio"]

if nome in list and hora <= 9:
    print(f"Senhor {nome} chegou cedo, consulta ainda não liberada")
elif nome in list and hora >= 10:
    print(f"Senhor {nome} liberado para consulta!")
elif idade >=60:
        print(f"Senhor {nome} aguardar encaixe de horario.") 
else:    
    print(f"Senhor {nome} não liberado para consulta no momento!")
    