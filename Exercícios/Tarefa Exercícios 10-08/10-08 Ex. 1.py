'''1) Faça um programa que verifique se um número é perfeito
ou não. Um número é dito perfeito quando ele é igual a soma
dos seus divisores excetuando ele próprio. (Ex: 6 é perfeito,
6 = 1 + 2 + 3, que são seus divisores). 
Exiba uma mensagem na tela informando se o número é ou não
perfeito.'''

num=int(input("Insira um número: "))
soma=0
for i in range (1, num):
    if num%i == 0:
        soma+=i
if soma==num:
    print("Número Perfeito!")
else:
    print("Número não perfeito")
