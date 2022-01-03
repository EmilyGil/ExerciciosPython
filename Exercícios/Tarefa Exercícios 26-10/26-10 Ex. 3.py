'''3)Faça um programa que preencha uma matriz 3 x 5, e depois calcule e mostre:
◦O maior elemento da matriz e em qual linha e coluna ele está armazenado (tem guardar os índices)
◦A média dos números ímpares da matriz
◦Mostre na tela todos os números primos, se houver.'''

import random
mat=[]
lin=col=somaImpar=qtdImpar=0
primos=[]
for i in range(3):
    linha=[]
    for j in range(5):
        linha.append(random.randint(1, 50))
    mat.append(linha)

print("======== MATRIZ 3x5 =========")
for i in range(3):
    print(mat[i])

maior=mat[0][0]

for i in range(3):
    for j in range(5):
        if mat[i][j]>maior:
            maior=mat[i][j]
            lin=i
            col=j
        if mat[i][j]%2!=0:
            somaImpar+=mat[i][j]
            qtdImpar+=1
        
        div=0
        for k in range(1, mat[i][j]+1):
            if mat[i][j]%k==0:
                div+=1
        if div==2:
            primos.append(mat[i][j])
        
mediaImpar=somaImpar/qtdImpar

print("\nMaior elemento da matriz:", maior, "- Linha", lin, ", coluna", col)
print("Média dos números ímpares: %.2f" %mediaImpar)
print("Números primos:", primos)
