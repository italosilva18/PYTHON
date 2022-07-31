#Faça um programa que leia uma valor dia hora minutos e segundos do usuario . Imprima o total em segundos:

print( "Exercicio 3.9")
dia=int(input("Digite a quantidade de dias:"))
hora=dia*24
minutos=hora*60
segundos=minutos*60
total1=(segundos)
hora=int(input("Digite a quantidade de horas:"))
minutos=hora*60
segundos=minutos*60
total2=(segundos)
minutos=int(input("Digite a quantidade de minutos:"))
segundos=minutos*60
total3=(segundos)
segundos=int(input("Digite a quantidade de segundos:"))
total4=(segundos)
total=(total1 + total2 + total3 + total4)
print(f"total em segundos é:{total}segundos")