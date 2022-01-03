'''Escreva um programa que preencha uma matriz 4 x 3 com números inteiros, calcule e mostre na tela:
a) A soma dos elementos que estão na 2ª e 4ª linha da matriz
b) A soma dos números primos
'''
import random
mat=[]
for i in range(4):
    linha=[]
    for j in range(3):
        linha.append(random.randint(1, 100))
    mat.append(linha)

for i in range(4):
    print(mat[i])

soma=0
primos=0
for i in range(4):
    for j in range(3):
        if i==1 or i==3:
            soma+=mat[i][j]
        div=0
        for k in range(1, mat[i][j] + 1):
            if mat[i][j] % k == 0:
                div += 1
        if div == 2:
            primos+=mat[i][j]
print("\nSoma dos elementos da 2ª e 4ª linha:", soma)
print("Soma dos números primos:", primos)