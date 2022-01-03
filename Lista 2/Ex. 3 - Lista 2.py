'''Faça um programa que preencha duas listas, lista A e lista B com 5 números em cada. 
Gere a lista C, com os números da lista A e lista B. Depois calcule e mostre na tela a 
quantidade de números perfeitos. Um número é perfeito quando ele é igual a soma dos 
seus divisores excetuando ele próprio. (Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus 
divisores).'''

listaA=[]
listaB=[]
listaC=[]

for m in range(5):
    listaA.append(int(input("Insira número da lista A: ")))
for n in range(5):
    listaB.append(int(input("Insira número da lista B: ")))

listaC.extend(listaA)
for i in range(5):
    if listaB[i] not in listaC:
        listaC.append(listaB[i])
listaC.sort()

print("Lista A = ", listaA)
print("Lista B = ", listaB)
print("Lista C = ", listaC)

qtdPerfeito=0
for j in range(len(listaC)):
    soma=0
    for k in range(1, listaC[j]):
        if listaC[j]%k == 0:
            soma+=k
    if soma==listaC[j]:
        qtdPerfeito+=1
print("Quantidade de números perfeitos: ", qtdPerfeito)
