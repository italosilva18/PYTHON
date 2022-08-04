#Escreva um programa para aprovar o emprestimo bancario para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salario e a quantidade de anos a pagar.
# O valor da prestação mensal não pode ser superior a 30% do salario.
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

casa=float(input("Qual é o valor da casa a comprar: "))
salario=float(input("Qual é o valor do seu Salario: ")) 
anos=int(input("Qual é a quantidade de anos a ser paga?"))
meses=anos*12
prestação=casa/meses
conta=salario*30/100
if prestação<=conta:
    print(f"Eprestimo Aprovado!! e o valor da prestação é de R${prestação:6.2f} e a quantidade é: {meses} Meses.")
else:
    print(f"Infelismente seu Eprestimo não foi Aprovado!!")