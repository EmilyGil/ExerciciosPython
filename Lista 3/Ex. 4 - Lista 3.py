'''Escreva um programa que armazene em uma matriz, o nome e duas notas de 5 alunos.
Calcule e armazene em uma lista a média de cada aluno e em outra lista o status
(media >= 6, “aprovado”, caso contrário, “reprovado”)
faça uma opção para que o usuário possa fazer uma pesquisar por nome. Se
encontrar seja exibido na tela:
•	posição em que foi encontrado (índice);
•	nome do aluno;
•	as duas notas e a média;
•	status;
'''
import random
mat=[]
medias=[]
status=[]
nomes=[]
for i in range(5):
    linha=[]
    for j in range(3):
        if j==0:
            linha.append(input(str("Aluno: ")))
            nomes.append(linha[j])
        else:
            linha.append(random.randint(0, 10))
    mat.append(linha)
for i in range(5):
    print(mat[i])
    soma=mat[i][1]+mat[i][2]
    media=soma/2
    medias.append(media)
    if media>=6:
        status.append("aprovado")
    else:
        status.append("reprovado")
print("\nMédias:", medias)
print("Status:", status)

print("\nDigite o nome do aluno ou fim para encerrar:")
pesq=input(str("Consultar aluno: "))
while pesq!="fim":
    if pesq in nomes:
        idx=nomes.index(pesq)
        print("\nPosição (index):", idx)
        print("Nome:", pesq)
        print("Nota 1:", mat[idx][1])
        print("Nota 2:", mat[idx][2])
        print("Média:", medias[idx])
        print("Status:", status[idx])
    else:
        print("Aluno não encontrado!")
    pesq = input(str("\nConsultar aluno: "))