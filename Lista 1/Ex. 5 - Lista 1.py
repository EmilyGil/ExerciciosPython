'''5) Faça um programa que receba 10 números inteiros.
Calcule o fatorial de cada número e mostre na tela.
'''

for i in range(10):
    num=int(input("\nInsira um número: "))
    fat=1
    for j in range(1, num+1):
       fat*=j 
    print("Fatorial: ", fat)

