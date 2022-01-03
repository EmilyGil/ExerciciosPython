'''Crie uma função que receba uma lista X de 10 elementos como parâmetro e
retorne a soma dos elementos da lista.'''
import random

def soma(vetor):
    total=sum(vetor)
    return(total)

x=[]
for i in range(10):
    x.append(random.randint(1, 50))
print("Lista: ", x)
res=soma(x)
print("A soma dos elementos é ", res)
