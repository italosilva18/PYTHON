#Escreva um programa para calcular a redução de tempo de vida de um fumante.Pergunte a quantidade de cigarros fumados 
#por dia e quantos anos ele ja fumou considere que um fumante perde 10 minutos de vida a cada cigarro e calcule  
#quantos dias de vida um fumante perderá. Exiba o total em dias

print( "Exercicio 3.15")

cigarros = float(input("Digite a quantidade de cigarros fumados durante o dia: "))
anos = float(input("Digite a quantidade de anos que fumou: "))
dia = 1440
perde1 = cigarros*10
perde2 = anos*365
perde3 = perde1*perde2 
total= perde3//dia
print(f"O fumante Perderá o total de:{total}dias")