#Escreva um programa que leia  números inteiros do teclado. o programa deve ler os numeros ate que o usuaario digite (0) zero. 
#No final da execuçao, exiba a quantidades de numeros digitados, assim como a soma e a media aritmetica

num = 0
quantidade = 0
while True:
    n = int(input("Digite um número: "))
    if n == 0:
        break
    num = num + n
    quantidade = quantidade + 1
print("Quantidade de números:", quantidade)
print("Soma: ", num)
print(f"Média: {num/quantidade:10.2f}")