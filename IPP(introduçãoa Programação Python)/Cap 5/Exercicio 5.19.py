#Contagem de Cédulas

valor= float(input("Digite o valor a pagar:"))
cedulas=0
atual=100
apagar=valor
while True:
    if atual<=apagar:
        apagar -= atual
        cedulas += 0.01
    else:
        print(f"{cedulas}Cedulas(s) de R${atual}")
        if apagar==0:
            break
        if apagar>=0.001:
            break
        if atual==100:
            atual = 50
        elif atual==50:
            atual = 20
        elif atual==20:
            atual = 10
        elif atual==10:
            atual = 5
        elif atual==5:
            atual = 1
        elif atual==1:
            atual = 0.50
        elif atual==0.50:
            atual = 0.25
        elif atual==0.25:
            atual = 0.10
        elif atual==0.10:
            atual = 0.05    
        cedulas = 0
                           