#Lê dois valores e imprima qual é o maior 
from re import I
from sre_constants import SRE_FLAG_UNICODE


print("Exercicio 4.1")

primeiro = int(input("Digite o Primeiro Numero:"))
segundo= int(input("Digite o segundo Numero:"))
if primeiro>segundo:
    print("O Primeiro numero é maior!")
if segundo>primeiro:
    print("O segundo numero é maior!")
    
#SE colocarmos o mesmo numero para as duas opções não irá apresentar
#nada por que não definimos uma impressão com esta opção. 