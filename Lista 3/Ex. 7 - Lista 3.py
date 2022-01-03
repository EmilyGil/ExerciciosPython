'''A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
coletando dados sobre o salário, idade e o número de filhos. Escreva um programa que leia esses dados,
por exemplo para 10 pessoas. Armazene esses dados em uma matriz, depois calcule e mostre:
a) A média de salário da população
b) A média do número de filhos
c) A quantidade de filhos das pessoas que tem idade entre 15 a 25 anos
d) A média de salário de pessoas que tem idade entre 20 a 30 anos
'''
import random
mat=[]
somaSal=somaFil=qtdFilhos=somaD=qtdD=0
for i in range(4):
    linha=[]
    for j in range(10):
        if i==0:
            linha.append(input(str("Pessoa: ")))
        if i==1:
            salario=(random.randint(500, 4000))
            linha.append(salario)
            somaSal+=salario
        if i==2:
            linha.append(random.randint(15, 50))
        if i==3:
            filhos=(random.randint(1, 5))
            linha.append(filhos)
            somaFil+=filhos

    mat.append(linha)
for i in range(4):
    print(mat[i])

for j in range(10):
    if mat[2][j] > 15 and mat[2][j] < 25:
        qtdFilhos+=mat[3][j]
    if mat[2][j] > 20 and mat[2][j] < 30:
        somaD+=mat[1][j]
        qtdD+=1

mediaSal=somaSal/10
mediaFil=somaFil/10
mediaD=somaD/qtdD
print("\nMédia de salário da população:", mediaSal)
print("Média do número de filhos:", mediaFil)
print("Qtd de filhos das pessoas que tem idade entre 15 e 25 anos:", qtdFilhos)
print("Média de salários das pessoas com idade entre 20 e 30 anos: %.2f" %mediaD)