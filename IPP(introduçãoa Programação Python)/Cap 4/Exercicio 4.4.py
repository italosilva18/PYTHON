# Escreva um programa que pergunte o salario do funcionario e calcule o valor do aumento
#Para salarios superiores a R$ 1.250,00 calcule um aumento de 10%.Para os inferiores ou iguais,de 15%

salario=float(input("Digite o salario do funcionario:"))
valor=salario
salario1=(valor*15/100)
r1=salario1+salario
salario2=(valor*10/100)
r2=salario2+salario
if salario>1250:
    print(f"Seu salario teve um aumento de R$:{salario2:5.2f} e agora é de R$:{r2:5.2f}")
if salario<=1250:
    print(f"Seu salario teve um aumento de R$:{salario1:5.2f} e agora o novo valor que vc ira receber é de R$:{r1:5.2f}")