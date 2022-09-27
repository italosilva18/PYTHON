#Escreva um programa que pergunte o deposito inicial e a taxa de juros de uma poupaça 
# Exiba os valores Mês a mês para os 24 primeiros meses Escreva o total ganhos com juros no periodo 
# Que pergunte tambem um valor add a cada mes

deposito=float(input("Digite o Valor de Deposito Inicial: "))
taxa=float(input("Digite o Valor da Taxa de Juros: "))    
juros=deposito*taxa/100
mes=1
saldo=deposito
while mes<=24:
    saldo = saldo+juros
    print(f"Mês: {mes} é de R${saldo:5.2f}.")
    dm=float(input("Digite o Valor de no mes: "))
    saldo=saldo+dm
    mes=mes+1
print(f"O ganho com os juros foi R$: {saldo-deposito:5.2f}.")
    
    