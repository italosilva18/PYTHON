# Escreva um programa que leia três numeros e que imprima o maior e o menor.
print("Exercicio 4.1")

numero01= int(input("Digite um numero:"))
numero02= int(input("Digite o segundo numero:"))
numero03= int(input("Digite o terceiro numero:"))

if numero01>numero02<numero03:
    print("O maior numero é o Primeiro:")
    print("O menor numero é o Segundo:")
if numero02>numero01<numero03:
    print("O maior numero é o Segundo:")
    print("O menor numero é o Primeiro:")
if numero03>numero01>numero02:  
    print("O maior numero é o Terceiro:")
    print("O menor numero é o Segundo:")
if numero01>numero02>numero03:
    print("O maior numero é o Primeiro:")
    print("O menor numero é o Terceiro:")
if numero02>numero01>numero03:
    print("O maior numero é o Segundo:")
    print("O menor numero é o Terceiro:")
if numero03>numero01<numero02:  
    print("O maior numero é o Terceiro:")
    print("O menor numero é o Primeiro:")
