#Escreva um programa que leia dois numeros. imprima a divisão inteira do primero pelo segundo, assim como o resto da divisão. 
# Ultilize apenas os operadores de soma e subitração para calcular o resultado.

dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
quociente = 0
x = dividendo
while x >= divisor:
    x = x - divisor
    quociente = quociente + 1
resto = x
print(f"{dividendo} / {divisor} = {quociente} (quociente) {resto} (resto)")