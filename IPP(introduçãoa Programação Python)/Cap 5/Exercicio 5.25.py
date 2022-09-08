#Escreva um programa que calcule a raiz quadrada de um número. 
# Utilize o método de Newton para obter um resultado aproximado. 
# Sendo n o número a obter a raiz quadrada, considere a base b=2
# Calcule p usando a fórmula p=(b+(n/b))/2. Agora, calcule o quadrado de p.
# A cada passo, faça b=p e recalcule p usando a fórmula apresentada.
# Pare quando a diferença absoluta entre n e o quadrado de p for menor que 0,0001.


numero = float(input("Digite um número para encontrar a sua raiz quadrada: "))
b = 2
while abs(n - (b * b)) > 0.00001:
    p = (b + (numero / b)) / 2
    b = p
print(f"A raiz quadrada de {numero} é aproximadamente {p:8.4f}")