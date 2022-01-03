'''Escreva um programa que leia uma matriz 6 x 10, some as colunas individualmente e
acumule as somas na 7ª linha da matriz. O programa deverá mostrar o resultado de cada coluna.'''
import random
mat=[]
for i in range(6):
    linha=[]
    for j in range(10):
        linha.append(random.randint(1, 10))
    mat.append(linha)
print("\n=========MATRIZ 6x10============")
for i in range(6):
    print(mat[i])

linha7 = []
for j in range(10):
    soma = 0
    for i in range(6):
        soma+=mat[i][j]
    linha7.append(soma)
    print("Soma da coluna", j+1, "=", soma)
mat.append(linha7)
print("\n=========MATRIZ 7x10============")
for i in range(7):
    print(mat[i])

