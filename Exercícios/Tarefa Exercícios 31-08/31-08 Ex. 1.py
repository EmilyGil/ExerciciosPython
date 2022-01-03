'''Faça um programa que preencha uma lista com os nomes de 10 alunos,
e outra lista com a idade dos alunos. Calcule e mostre:
◦a quantidade de alunos que tem idade superior a 15;
◦a média das idades dos alunos;
◦a quantidade de alunos que tem idade abaixo da média;
◦a maior idade e o nome do aluno;
◦a menor idade e o nome do aluno.'''

from random import randint
nomes=[]
idades=[]
qtd15=0
qtdMenor=0
for i in range(10):
    nomes.append(str(input("\nNome: ")))
    idades.append(randint(10, 18))
    print("Idade: ", idades[i])

    if idades[i]>15:
        qtd15+=1

mediaIdades=(sum(idades))/(len(idades))
maiorIdade=idades[0]
menorIdade=idades[0]
idMaior=0
idMenor=0
for i in range(10):
    if idades[i]<mediaIdades:
        qtdMenor+=1

    if idades[i]>maiorIdade:
        maiorIdade=idades[i]
        idMaior=i

    if idades[i]<menorIdade:
        menorIdade=idades[i]
        idMenor=1

print("\n=========RESULTADOS============")
print("Qtd de alunos com idade superior a 15: ", qtd15)
print("Média das idades dos alunos: ", mediaIdades)
print("Qtd de alunos com idade abaixo da média: ", qtdMenor)
print("Maior idade: ", nomes[idMaior], " - ", maiorIdade)
print("Menor idade: ", nomes[idMenor], " - ", menorIdade)
