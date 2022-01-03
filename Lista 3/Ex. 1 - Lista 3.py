'''Escreva um programa que leia uma matriz de ordem 3 x 5 de elementos inteiros, 
calcule e mostre na tela:
a) menor número da matriz;
b) soma dos números múltiplos de 3 da matriz;
c) maior número da 3ª coluna da matriz (índice 2);
d) média dos números da matriz;'''

mat=[]
for i in range(3):
    linha=[]
    for j in range(5):
        linha.append(int(input("Insira um número: ")))
    mat.append(linha)

menor=mat[0][0]
soma=0
somaTotal=0
maiorCol=mat[0][2]
for i in range(3):
    for j in range(5):
        if mat[i][j] < menor:
            menor = mat[i][j]
        if mat[i][j]%3==0:
            soma+=mat[i][j]
        somaTotal+=mat[i][j]
for i in range(3):
    if mat[i][2]>maiorCol:
        maiorCol=mat[i][2]

media=somaTotal/15

print("\n======= MATRIZ =======")
for i in range(3):
    print(mat[i])

print("\na) Menor número da matriz:", menor)
print("b) soma dos números múltiplos de 3 da matriz:", soma)
print("c) maior número da 3ª coluna da matriz:", maiorCol)
print("d) média dos números da matriz: %.2f" %media)