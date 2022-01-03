''' Escreva um programa que leia a idade de 10 pessoas e armazene-as em uma lista.
Calcule e mostre:
a) a menor idade
b) a média das idades
c) a quantidade de pessoas que tem idade entre 20 e 30 anos (inclusive)
d) a quantidade de pessoas com idade maior que a média'''

from random import randint

idade=[]
qtdC=qtdD=0
for i in range(10):
    idade.append(randint(10, 100))
    print("Idade: ", idade[i])
    if idade[i]>=20 and idade[i]<=30:
        qtdC+=1

print("\nIdades: ", idade)

menor=min(idade)
media=(sum(idade))/(len(idade))

for j in range(10):
    if idade[j]>media:
        qtdD+=1

print("\na)Menor idade: ", menor)
print("b)Média das idades: ", media)
print("c)Qtd de pessoas com idade entre 20 e 30 anos: ", qtdC)
print("d)Qtd de pessoas com idade maior que a média: ", qtdD)



