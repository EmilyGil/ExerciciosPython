'''Escreva um programa que preencha uma matriz 4 x 6 com números inteiros,
calcule e mostre na tela:
a) A quantidade de números que estão no intervalo entre 10 e 30
b) A soma dos números maiores que 10 e pares
c) A soma dos números que estão na quarta coluna da matriz
d) A média dos números da matriz que estão na terceira linha
'''

import random
mat=[]
for i in range(4):
    linha=[]
    for j in range(6):
        linha.append(random.randint(0, 100))
    mat.append(linha)

print("\n======= MATRIZ 4X6 =======")
for i in range(4):
    print(mat[i])

qtd=0
somaB=0
somaC=0
somaD=0
for i in range(4):
    for j in range(6):
        if (mat[i][j] > 10) and (mat[i][j] < 30):
            qtd+=1
        if (mat[i][j]>10) and (mat[i][j]%2==0):
            somaB+=mat[i][j]

for i in range(4):
    somaC+=mat[i][3]
for j in range(6):
    somaD+=mat[2][j]
mediaD=somaD/6

print("\na) A quantidade de números que estão no intervalo entre 10 e 30:", qtd)
print("b) A soma dos números maiores que 10 e pares:", somaB)
print("c) A soma dos números que estão na quarta coluna da matriz:", somaC)
print("d) A média dos números da matriz que estão na terceira linha: %.2f" %mediaD)
