'''1) Faça um programa  que receba 10 números inteiros e armazene numa lista.
calcule e mostre:

◦A quantidade de números pares;
◦A soma dos números ímpares;
◦A quantidade de números entre 10 e 20 (inclusive);
◦A média dos números da lista.'''

lista=[]
qtd_par=soma_impar=qtd=0

for i in range(10):
    num=int(input("Insira o número: "))
    lista.append(num)
    if num%2==0:
        qtd_par+=1
    else:
        soma_impar+=num
    if num>=10 and num<=20:
        qtd+=1
        
media=(sum(lista))/(len(lista))
print("====================")
print(lista)
print("\nQuantidade de números pares: ", qtd_par)
print("Soma dos números ímpares: ", soma_impar)
print("Quantidade de números entre 10 e 20: ", qtd)
print("Média dos números da lista: ", media)


''' ==========CORREÇÃO=========='''
'''from random import randint
num=[]
for i in range(10):
    num.append(randint(1,30)

print(num)
qt_par=soma_imp=qtd_media=0
for i in range(len(num)):
    if num[i] % 2 == 0:
        qt_par+=1
    else:
        soma_imp+=num[i]

    if num[i] >= 10 and num[i]<=20:
        qtd+=1

media=sum(um)/len(num)

print("Qtde pares: ", qt_par)
print("Soma ímpares: ", soma_imp)
print("Qtde de números entre 10 e 20: ", qtd)
print("Média: ", media) '''

