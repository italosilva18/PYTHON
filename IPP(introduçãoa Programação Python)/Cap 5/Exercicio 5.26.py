#Escreva um programa que calcule o resto da divisão inteira entre dois números. 
# Utilize apenas as operações de soma e subtração para calcular o resultado

dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
quociente = 0
x = dividendo
while x >= divisor:
    x = x - divisor
    quociente = quociente + 1
resto = x
print(f"O resto de {dividendo} / {divisor} é {resto}")