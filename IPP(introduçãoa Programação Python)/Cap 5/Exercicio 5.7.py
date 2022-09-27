#Modifique o programa anterior de forma que o usuario tambem digite o inicio e o fim da taboada 
# em vex de começar com 1 e terminar com 10


inicio=int(input("digite o numero que vai iniciar a taboada: "))
tables=int(input("digite o numero que vai ser multiplicado: "))
fim = int(input("Digite ate quanto vai terminar taboada: "))  

while inicio <= fim:
    print(tables*inicio)
    inicio=inicio+1
    