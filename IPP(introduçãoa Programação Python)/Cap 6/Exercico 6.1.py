#Modifique o programa anterior para ler 7 notas ao em vez de 5


notas=[0,0,0,0,0]
soma=0
x=0
while x<5:
    notas[x] = float(input(f"nota{x}:"))
    soma+=1
x=0
while x < 5:
    print(f"Nota{x}:{notas[x]:6.2f}")
    x+=1
print(f"Média:{soma/x:5.2f}")
