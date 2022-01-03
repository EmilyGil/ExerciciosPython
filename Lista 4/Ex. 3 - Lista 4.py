'''Um time de basquete possui 12 jogadores. Faça um programa que preencha uma matriz com o nome e a
altura dos jogadores, e através de uma função faça os seguintes cálculos:
a. o nome e a altura do jogador mais alto
b. a média de altura do time
Obs: a função deverá receber por parâmetro a matriz e imprimir os resultados dentro da função
'''

mat=[]

def funcaoMatriz(lin, col):
    maiorJog=mat[0][1]
    nomeMaiorJog=''
    somaAlt=0
    for i in range(lin):
        if mat[i][1] > maiorJog:
            maiorJog=mat[i][1]
            nomeMaiorJog=mat[i][0]
        somaAlt+=mat[i][1]
    mediaAlt=somaAlt/lin
    print("\nJogador mais alto: ", nomeMaiorJog, "-", maiorJog, "m")
    print("Média de altura dos jogadores: %.2f" %mediaAlt)

print("========PROGRAMA PRINCIPAL===========")
for i in range(12):
    linha=[]
    for j in range(1):
        nome=str(input(f"Jogador {i+1}: "))
        alt=float(input(f"Altura do jogador {i+1}: "))
        linha.append(nome.upper())
        linha.append(alt)
    mat.append(linha)

print("\n=======MATRIZ JOGADORES=======")
for i in range(12):
    print(mat[i])

res=funcaoMatriz(12, 2)
