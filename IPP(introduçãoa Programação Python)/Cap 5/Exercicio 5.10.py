
pontos=0
questao=1

while questao <= 3:
    resposta=input(f"Digite a Resposta da questão{questao}: ")
    if questao == 1 and (resposta =="b"or resposta == "B"):
        pontos = pontos+1
    if questao == 2 and (resposta =="a"or resposta == "A"):
        pontos = pontos+1
    if questao == 3 and (resposta =="c"or resposta == "C"):
       pontos=pontos+1
    questao=questao+1
print(f"O aluno Fez: {pontos} Pontos(s)") 
    