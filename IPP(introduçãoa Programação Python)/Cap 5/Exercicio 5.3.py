#Faça um programa para escrever  a contagem regressiva do lançamento de um foguete. 
#O programa deve Imprimir (8,7,6,5,4,3,2,1,0,fogo!!) na tela

x=int(input("Digite o valor da contagem: "))
while x>=0:
    print(x)
    x=x-1
    if x==-1:
        print("fogo!!!")