#Escreva um programa que pergunte a quantidade de quilometros percorridos por um carro alugado pelo usuario
#assim a quntidade de dias pelos quais o veiculo foi alugado. calcule o preço a pagar sabendo que o carro custa 
#60 reis por dia e 0,15 por quilometro rodado 
print( "Exercicio 3.14")

percorridos = float(input("Digite a quilometragem percorridados: "))
dias=   float(input("Digite a quantidade de Dias que foi ultilizado: "))  
Total =(percorridos*0.15+dias*60)
print(f"Valor total a ser pargo pelo Usuario é de: R${Total:5.2f}")
