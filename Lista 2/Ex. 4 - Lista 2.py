''' Faça um programa que preencha duas listas com 10 elementos em cada.Depois percorra 
essas duas listas e gere uma terceira lista com os números que se repetem nas duas listas. 
Mostre as três listas na tela'''
import random

listaA=[]
listaB=[]
listaC=[]

for i in range(10):
    listaA.append(random.randint(1,50))
    listaB.append(random.randint(1,50))

listaA.sort()
listaB.sort()

for j in listaA:
    for k in listaB:
        if j==k:
            listaC.append(j)

print("Lista A = ", listaA)
print("Lista B = ", listaB)
print("Lista C = ", listaC)
