'''2) Faça um programa que preencha uma lista com os nomes de 10 alunos,
e outra lista com a idade dos alunos. Calcule e mostre:
◦a quantidade de alunos que tem idade superior a 15;
◦a média das idades dos alunos;
◦a quantidade de alunos que tem idade abaixo da média;'''

nomes=[]
idades=[]

for i in range(10):
    nomes.append(str(input("Insira o nome do aluno: ")))
    idades.append(int(input("Informe a idade de " + nomes[i] +": ")))

media=(sum(idades))/(len(idades))
qtd_15=qtd_media=0
for i in range(10):
    if idades[i]>15:
        qtd_15+=1
    if idades[i]<media:
        qtd_media+=1

print("\n===================")
print("Qtd de alunos com idade superior a 15: ", qtd_15)
print("Média das idades dos alunos: ", media)
print("Qtd de alunos com idade abaixo da média: ", qtd_media)


'''=========CORREÇÃO=========='''
'''
from random import randint
nomes=[]
idade=[]
for i in range(5):
    nomes.append(str(input("Nome: ")))
    idade.append(randint(1, 30))

print(nomes)
print(idade)
qtd_15=media=cont=0
media=sum(idade)/len(idade)

maior=idade[0]
pos=0

for i in range(5):
    if idade[i] > maior:
        maior=idade[i]
        pos=i

    if idade[i]>15:
        qtd_15+=1

    if idade[i]<media:
        cont+=1

print("Média: ", media)
print("Qtde de alunos > 15: ", qtd_15)
print("Qtde alunos < media: ", cont)
print("Aluno com maior idade: ", maior, " - Nome: ", nome[pos])
'''
