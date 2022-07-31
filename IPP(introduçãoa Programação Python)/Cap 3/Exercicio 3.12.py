#Faça um programa que calcule o tempo de uma viagem de carro.
# Pergunte a distancia a percorrer e a velocidade media esperada para a viagem
from dis import dis


print( "Exercicio 3.12")

distancia = float(input("Insira a Distancia a Percorrer:"))
velocidade = float(input("Qual é a Velocidade meia do trageto:"))
tempo=distancia/velocidade
print(f"O tempo de sua viagem será de:{tempo:3.2f}h/m.")
