'''Escreva um programa que preencha uma lista com os nomes de 10 alunos,
e outra lista com a média dos alunos. Calcule e mostre:
a) a média da classe;
b) a quantidade de alunos que tiveram média igual ou superior a 7;
c) a quantidade de alunos que tiveram média abaixo de 7;
d) a maior média da classe e nome do aluno que obteve a maior média;
'''
import random
nomes=[]
medias=[]
qtdMaior=qtdMenor=0
for i in range(10):
    nomes.append(input(str("Nome: ")))
    medias.append(random.randint(0, 10))
print("Nomes:", nomes)
print("Médias:", medias)
mediaClasse=(sum(medias))/(len(medias))
for i in range(10):
    if medias[i] >= 7:
        qtdMaior+=1
    else:
        qtdMenor+=1
maiorM=max(medias)
idx=medias.index(maiorM)
print("\nMédia da classe: %.2f" %mediaClasse)
print("Qtd de alunos com média igual ou superior a 7:", qtdMaior)
print("Qtd de alunos com média abaixo de 7:", qtdMenor)
print("Maior média da classe:", maiorM, "- Aluno:", nomes[idx])