# Escreva um programa que leia três numeros e que imprima o maior e o menor.
print("Exercicio 4.1")
numero01= int(input("Digite um numero:"))
numero02= int(input("Digite o segundo numero:"))
numero03= int(input("Digite o terceiro numero:"))
maior= numero01

if numero02>numero03 and numero02>numero01:
   maior=numero02
if numero03>numero02 and numero03>numero01:
    maior=numero03

menor= numero01
if numero02<numero03 and numero02<numero01:
   menor=numero02
if numero03<numero02 and numero03<numero01:
    menor=numero03

print(f"O maior numero digitado é:{maior}")
print(f"O menor numero digitado é:{menor}")

