'''Escreva um programa que leia uma matriz de ordem 5 x 4, onde na 1ª coluna da matriz é armazenado
o nome do vendedor, da 2ª coluna a 4ª coluna são armazenados o total de vendas por mês de cada vendedor,
portanto na 2ª coluna é armazenado a venda do mês 1, 3ª coluna do mês 2 e na 4ª coluna do mês 3.
Calcule e mostre na tela:
a) O valor total vendido por vendedor
b) A maior venda do mês 1
c) A menor venda do mês 3
d) O total vendido por mês de todos os vendedores
'''
import random
matA=[]
for i in range(5):
    linha=[]
    for j in range(4):
        if j==0:
            linha.append(input(str("Vendedor: ")))
        else:
            linha.append(random.randint(1000, 10000))
    matA.append(linha)
for i in range(5):
    print(matA[i])

print("\nValor total de vendas por vendedor:")
for i in range(5):
    soma = 0
    for j in range(4):
        if j!=0:
            soma+=matA[i][j]
    print(matA[i][0], "- R$", soma)

maiorV=matA[0][1]
menorV=matA[0][3]
total1=total2=total3=0
for i in range(5):
    for j in range(4):
        if matA[i][1] > maiorV:
            maiorV=matA[i][1]
        if matA[i][3] < menorV:
            menorV=matA[i][3]
    total1 += matA[i][1]
    total2 += matA[i][2]
    total3 += matA[i][3]
print("\nMaior venda do mês 1: ", maiorV)
print("Menor venda do mês 3: ", menorV)
print("Total vendido por mês:")
print("Mês 1 = R$", total1)
print("Mês 2 = R$", total2)
print("Mês 3 = R$", total3)
