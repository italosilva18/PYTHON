#Escreva um programa que pergunte a velocidade do carro de um usuário.
# Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado.
# Neste caso Exiba o valor da multa, cobrando R$5 por km acima de 80km/h.
print("Exercicio 4.1")

velocidade= float(input("Digite a velocidade que estava transitando?")) 
resto= velocidade-80
pagamento = resto*5
if velocidade>80:
    print(f"Voce foi Multado!,E o valor da Infração é de R$:{pagamento:5.2f}")
