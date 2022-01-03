'''1) Faça um programa que receba 5 números inteiros. Calcule e mostre:

◦A soma dos números primos
◦Mostre na tela os números primos'''

soma=0
for i in range(5):
    num=int(input("Insira o número: "))
    div=0
    for j in range(1, num+1):
        if num%j==0:
            div+=1

    if div==2:
        print("Número primo")
        soma+=num
    else:
        print("Não primo")

print("\nSoma dos números primos: ", soma)
        
