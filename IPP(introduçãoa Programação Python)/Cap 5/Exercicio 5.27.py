#Escreva um programa que verifique se um número é palíndromo. 
# Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos.
# Exemplos: 454, 10501

s = input("Digite o número a verificar, sem espaços:")
i = 0
f = len(s)-1  # posição do último caracter da string
while f > i and s[i] == s[f]:
    f = f - 1
    i = i + 1
if s[i] == s[f]:
    print(f"{s} é palíndromo")
else:
    print(f"{s} não é palíndromo")