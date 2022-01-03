''' Faça um programa que percorra duas listas e gere uma terceira lista sem os elementos 
repetidos. Mostra na tela as 3 listas.'''
import random
listaA=[]
listaB=[]
listaC=[]

for i in range(5):
    listaA.append(random.randint(1,50))
    listaB.append(random.randint(1,50))
listaA.sort()
listaB.sort()
for m in range(5):
    listaC.append(listaA[m])
    listaC.append(listaB[m])
for j in listaA:
    for k in listaB:
        if j==k:
            listaC.remove(j)
            listaC.remove(k)
listaC.sort()
print("Lista A = ", listaA)
print("Lista B = ", listaB)
print("Lista C = ", listaC)
