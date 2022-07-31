# Exercicio 3.1 - Complete a taabela a seguir, marcando inteiro ou flutuante dependando do numero apresentado 
from re import S, T
import re


print( "Exercicio 3.1")
print("5 int", "5.0 float","4.3 float","-2 int","100 int","1.333 float")
# Exercicio 3.2 - Complete a taabela a seguir, respondendo True ou False considere(a=4,b=10,c=5.0, d=1 e f=5) 
print( "Exercicio 3.2")
a=4
b=10
c=5.0 
d=1 
f=5
print(a==c, a<b, d>b, c!=f,a==b, c<d, b>a, c>=f, f>=c, c<=c,c<=f)
# Exercicio 3.3 - Complete a taabela a seguir utilizando ( a=True, b=False, c=True )  
print( "Exercicio 3.3")
a=True 
b=False 
c=True
print( a and a, b and b, not c, not b, not a, a and c, b and c, a or c,b or c,c or a,c or b,c or c,b or b)
# Exercicio 3.4 - Escreva um expressão para determinar se uma pessoa deve ou não pagar imposto. 
# #Considereque pagam imposto pessoas cujo o salario é mair que R$1200.
print( "Exercicio 3.4")
Salario = 1300
print(Salario>1200)
# Exercicio 3.5 -  Calcule o resultado da expressão a > b and c or d, ultilizando os valores da tabela a seguir:
print( "Exercicio 3.5")
a=(1, 10, 5)
b=(2, 3, 1)
c=(True, False, True)
d=(False, False, True)
print(a>b and c or d) 
# Exercicio 3.6 - Escreva uma expressão que será utilizada para descidir se um aluno foi ou não aprovado.
# Para ser aprovado, todas as medias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas Três Matérias,
# e que a nota de cada uma está armazenada nas seguintes variáveis: materia 1, 2,3   
print( "Exercicio 3.6")
materia1 = 6
materia2 = 8
materia3 = 9
media=7
total=((materia1+materia2+materia3)/3)
aprovado=total>=media
print(aprovado)


