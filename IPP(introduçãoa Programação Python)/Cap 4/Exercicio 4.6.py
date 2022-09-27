#Escreva um programa que pergunte a distancia que um passageiro deseja percorrer em km.
#Calcule o preço da passagem, cobrando R$0,50 por km para viagens de ate 200km e 0,45 para viagens mais longas!

print("Exercicio 4.6")
percuso=float(input("Qual é distância que deseja percorrer: "))
if percuso>200:
    passagem=percuso*0.45
else:
    passagem = percuso*0.50
print(f"O valor da passagem é de R$:{passagem:5.2f} e a quilometragem é de {percuso}km.")    

