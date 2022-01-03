'''3) Escreva um programa que leia um conjunto de 10 números inteiros
e armazene em uma lista. Calcule e mostre:
◦o menor número da lista e em qual posição está (índice)
◦a percentagem de números pares
◦a média dos números ímpares e maiores que 15
◦ a quantidade de números maiores que a média'''

from random import randint

lista=[]
qtdPar=qtdImpar=somaImpar=0
for i in range(10):
    lista.append(randint(1, 100))
    print("Número:", lista[i])
    if lista[i]%2==0:
        qtdPar+=1
    if lista[i]%2!=0 and lista[i]>15:
        qtdImpar+=1
        somaImpar+=lista[i]

menor=min(lista)        
porc=(qtdPar*100)/(len(lista))
mediaImpar=somaImpar/qtdImpar
media=sum(lista)/len(lista)
qtd=0
for i in range(10):
    if lista[i]>media:
        qtd+=1

print("\nLista: ", lista)
print("Menor número: ", menor, "- que se encontra na posição", lista.index(menor))
print("Porcentagem de números pares: ", porc)
print("Média dos ímpares maiores que 15: %.2f" %mediaImpar)
print("Quantidade de números maiores que a média: ", qtd)



