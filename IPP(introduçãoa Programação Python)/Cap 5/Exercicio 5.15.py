#Escreva um programa para controlar uma pequena maquina registradora. 
# Você deve solicitar ao usuario que digite o codigo do produtoe a quantidade comprada .
# Ultilize a tabela de codigos a seguir para obter o preço de cada produto: 
#  _________________________________
# |codigo | 1  | 2  | 3  | 5  | 9  |  
# |-------|----|----|----|----|----|
# |Preco  |0,50|1,00|4,00|7,00|8,00| 
# **********************************
# Seu programa deve exibir o total das compras depois que o usuario digitar 0 e
# qualquer outo codigo deve gerar a mensagem de erro "codigo"

apagar = 0
while True:
    codigo = float(input("Digite um Codigo: "))
    preço = 0
    if codigo==1:
        preço=0.50
    elif codigo==2:
        preço=1.00
    elif codigo==3:
        preço=4.00
    elif codigo==5:
        preço=7.00
    elif codigo==9:
        preço=8.00
    elif codigo==0:
        break
    else:
        print("Error:(Codigo Invalido)")
    if preço != 0:
        quantidade=float(input("Quantidade: "))
        apagar=apagar + (preço * quantidade)
print(f"Total a pagar R${apagar:8.2f}")