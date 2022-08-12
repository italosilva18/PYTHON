#Escreva um programa que leia dois numero. imprima o resultado da multiplicação do primeiro pelo segundo,
# ultilize apenas os operadores de soma e subtração para calcular o resultad. 
# Lembre-se de que podemos entender a multiplicação de dois numeros  como sumas sucessivas de um deles. Assim, 4x5=5+5+5+5=4+4+4+4+4

p = int(input("Primeiro número: "))
s = int(input("Segundo número: "))
x = 1
r = 0
while x <= s:
    r = r + p
    x = x + 1
print(f"{p} x {s} = {r}")