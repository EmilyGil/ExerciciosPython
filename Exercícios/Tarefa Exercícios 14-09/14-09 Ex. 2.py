'''2.Faça um programa que leia 10 números inteiros e
armazene-os na lista A.
Encontre o menor número da lista A e gere a lista B,
que é a multiplicação de cada elemento da lista A pelo
menor número.
Gere a lista C que é a união da lista A e a lista B.
Mostre as 3 listas na tela.'''

from random import randint
listaA=[]
listaB=[]
listaC=[]

for i in range(10):
    listaA.append(randint(1, 50))
    print("Número: ", listaA[i])
    '''listaA.append(int(input("Número: ")))'''

menorA=min(listaA)

for j in range(10):
    num=listaA[j]
    mult=num*menorA
    listaB.append(mult)

for k in range(10):
    listaC.append(listaA[k])
for l in range(10):
    listaC.append(listaB[l])

print("A: ", listaA)
print("B: ", listaB)
print("C: ", listaC)
