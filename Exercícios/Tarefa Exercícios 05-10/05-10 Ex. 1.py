'''Faça um programa que leia duas matrizes A e B 2x2 de inteiros e
imprima a matriz C que é a soma das matrizes A e B.'''
mat_A=[]
mat_B=[]
mat_C=[]
print("\nPreenchendo a matriz A: ")
for i in range(2):
    linha=[]
    for j in range(2):
        linha.append(float(input("Número: ")))
    mat_A.append(linha)

print("\nPreenchendo a matriz B: ")
for i in range(2):
    linha=[]
    for j in range(2):
        linha.append(float(input("Número: ")))
    mat_B.append(linha)

print("\n=========== SOMA DA MATRIZ A + MATRIZ B ===========")
for i in range(2):
    linha=[]
    for j in range(2):
        linha.append(mat_A[i][j] + mat_B[i][j])
    mat_C.append(linha)
for i in range(2):
    print(mat_C[i])
