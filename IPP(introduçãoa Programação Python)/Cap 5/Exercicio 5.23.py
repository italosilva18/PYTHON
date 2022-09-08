#Ecreva um programa que leia um numero e verifique se é ou não um numero primo.
# Para fazer essa verificação , calcule o resto da divisão do numero por 2 e depois por todos os numeros impares ate o numero ser lido. 
# Se o resto de uma dessas divisões for igual a zero, o numero não é primo.Observe que o 0 e 1 não são primos e que 2 é o unico numero primo que é par.

numero = int(input("Digite um número:"))
if numero < 0:
    print("Número inválido. Digite apenas valores positivos")
if numero == 0 or numero == 1:
    print(f"{numero} é um caso especial.")
else:
    if numero == 2:
        print("2 é primo")
    elif numero % 2 == 0:
        print(f"{numero} não é primo, pois 2 é o único número par primo.")
    else:
        x = 3
        while(x < numero):
            if numero % x == 0:
                break
            x = x + 2
        if x == numero:
            print(f"{numero} é primo")
        else:
            print(f"{numero} não é primo, pois é divisível por {x}")