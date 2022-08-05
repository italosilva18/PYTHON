#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia eletrica.
#Pergunte a quantidade de kwh consumida e o tipo de instalação: (R)para residencia (I) para industrias e (C) para comercio.
#Calcule o preço a pagar de acordo com a tabela a seguir.

import string


kwh = int(input("Qual a quantidade de kwh consumida: "))
print("Opções:")
print("Digite (R) para residencia")
print("Digite (I) para industrias")
print("Digite (C) para comercio")
opcoes= input("Digite uma das Opção Acima:")
if opcoes == "R":
   if kwh<=500:
       valor=0.40
   else:
       valor=0.65
elif opcoes =="I":
    if kwh<=1000:
        valor=0.55
    else:
        valor=0.60
elif opcoes=="C":
    if kwh<=5000:
        valor=0.55
    else:
        valor=0.60
else:
    print("categoria invalida digite uma das opção acima:")
    valor=0.
total=kwh*valor
print(f"O valor a ser pago é de R$:{total:6.2f}")