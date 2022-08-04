#Escreva um programa que leia dois numeros e que pergunte qual operação voce deseja realizar.
#Voce deve poder calcular soma, subitração, multiplicação e divisão. Exiba o resultado da operação solicitada.
numero1=float(input("Digite o primeiro numero: "))
numero2=float(input("Digite o segundo numero: "))
print("Para soma Digite ( 1 )")
print("Para subtração Digite ( 2 )")
print("Para Multiplicação Digite ( 3 )")
print("Para Divisão Digite ( 4 )")
operacao=float(input("Digite a Operação: "))

if operacao==1:
    r=numero1+numero2
elif operacao==2:
    r=numero1-numero2 
elif operacao==3:
    r=numero1*numero2
elif operacao==4:
    r=numero1/numero2
else :
    print("Voce deve digitar algum valor para que possamos continuar!" )
print(f"O resultado da Operação é:{r:6.2f}")