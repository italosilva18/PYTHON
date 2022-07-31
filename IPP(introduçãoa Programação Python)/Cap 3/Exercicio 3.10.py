#Faça um programa que calcule o aumento de um sálario.Ele deve Solicitar o valo do salario
#e a porcentagem do aumento.Exiba o valor do aumento e do novo salario.

salario=float(input("Digite o valor do seu salario:"))
porcentagem=float(input("Digite o valor da porcentagem de aumento: "))
aumento=(salario*porcentagem)/100
novoSalario=(salario+aumento)
print(f"O Valor do novo salario é:R${novoSalario:5.2f} e o aumento foi de R${aumento:5.2f}")
 