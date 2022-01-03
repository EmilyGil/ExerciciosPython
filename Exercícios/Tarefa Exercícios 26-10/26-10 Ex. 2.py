'''2) Faça um programa que, leia uma matriz 4x3 com os números inteiros. Calcule e mostre na tela:

◦A média dos números da 3ª linha (índice 2)
◦A soma dos números da 2ª coluna (índice 1)
◦A quantidade de números maiores que 5 e menores que 15 armazenados na matriz
◦Crie um vetor e armazene os números dessa matriz no vetor, mostrando na tela o resultado'''

import random

mat=[]
soma=qtd=0
v=[]

for i in range(4):
    linha=[]
    for j in range(3):
        linha.append(random.randint(1, 50))
    mat.append(linha)

print("========== MATRIZ 4X3 ============")
for i in range(4):
    print(mat[i])
    soma+=mat[i][1]

for i in range(4):
    for j in range(3):
        if mat[i][j]>5 and mat[i][j]<15:
            qtd+=1
        v.append(mat[i][j])

media=(sum(mat[2]))/(len(mat[2]))

print("\nMédia dos números da 3ª linha: %.2f" %media)
print("Soma dos números da 2ª coluna:", soma)
print("Qtd de números entre 5 e 15:", qtd)
print("Números: ", v)
