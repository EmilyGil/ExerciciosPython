'''.A prefeitura de uma cidade fez uma pesquisa entre 10 habitantes,
coletando dados sobre o salário e o número de filhos, armazene os
salários e número de filhos em listas. Faça um programa que calcule e mostre:
◦média de salário da população;
◦média do número de filhos;
◦maior salário;
◦percentual de pessoas com salário inferior a R$ 1000,00.'''

from random import randint

salarios=[]
filhos=[]
qtd=0
for i in range(10):
    salarios.append(float(input("Salário: ")))
    filhos.append(randint(1, 5))
    print(filhos[i])
    if salarios[i]<1000:
        qtd+=1
        
mediaS=sum(salarios)/len(salarios)
mediaF=sum(filhos)/len(filhos)
maiorS=max(salarios)
perc=(qtd*100)/len(salarios)

print("\n=========================")
print("Média de salários: ", mediaS)
print("Média do número de filhos: ", mediaF)
print("Maior salário: ", maiorS)
print("Percentual com salário inferior a R$1.000,00: ", perc)
