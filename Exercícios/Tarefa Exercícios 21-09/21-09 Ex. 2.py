'''(Exercício 2) Faça uma programa que leia 2 listas de números inteiros,
tendo cada um 10 e 20 elementos (pode ser usado a função randint) e apresente
na tela os elementos que não são comuns nas duas listas.'''
import random
listaA=[]
listaB=[]

for i in range(10):
    n=random.randint(0, 100)
    listaA.append(n)
print("Lista 1 = ", listaA)

for i in range(20):
    n=random.randint(0, 100)
    listaB.append(n)
print("Lista 2 = ", listaB)

dif=[]
for i in range(10):
    num=listaA[i]
    if (num in listaB) == False:
        dif.append(num)
for i in range(20):
    num=listaB[i]
    if (num in listaA) == False and (num in dif) == False:
        dif.append(num)

print("\nElementos que NÃO são comuns entre as listas: ", dif)



