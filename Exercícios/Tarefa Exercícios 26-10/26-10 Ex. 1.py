import random
mat=[]
qtdMult=somaPar=somaTotal=qtdTotal=0

for i in range(5):
    linha=[]
    for j in range(3):
        linha.append(random.randint(1, 100))
    mat.append(linha)

print("======= MATRIZ 5X3 ========")
for i in range(5):
    print(mat[i])

for i in range(5):
    for j in range(3):
        if mat[i][j]%3==0:
            qtdMult+=1
        if (mat[i][j]%2==0) and (mat[i][j]>10):
            somaPar+=mat[i][j]
        somaTotal+=mat[i][j]
        qtdTotal+=1
media=somaTotal/qtdTotal

print("\nQuantidade de múltiplos de 3:", qtdMult)
print("Soma dos pares e maiores que 10:", somaPar)
print("Média dos números armazenados na matriz: %.2f" %media)
