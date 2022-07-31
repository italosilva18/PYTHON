#Faça um programa que solicite um preço de uma mercadoria e o percentual de desconto.
#Exiba o valor do Desconto e o preço a pagar
print( "Exercicio 3.11")

preco=float(input("Digite o valor da Mercadoria:"))
desconto=float(input("Digite o Desconto da Mercador:"))
vdesconto=(preco*desconto)/100
novoPreco=preco-vdesconto
print(f"O valar do desconto é de R$:{vdesconto:5.2f} e o novo preco e de R$:{novoPreco:5.2f}")