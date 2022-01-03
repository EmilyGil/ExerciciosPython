''' Escreva um programa que gere uma lista que é resultado do produto de duas listas L1 e 
L2. Mostre na tela as 3 listas'''
import random
listaA=[]
listaB=[]
listaC=[]

for i in range(5):
    listaA.append(random.randint(1, 10))
    listaB.append(random.randint(1, 10))
    listaC.append(listaA[i]*listaB[i])

print("Lista A = ", listaA)
print("Lista B = ", listaB)
print("Lista C = ", listaC)
