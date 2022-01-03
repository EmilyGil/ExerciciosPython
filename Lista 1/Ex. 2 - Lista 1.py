'''2) Faça um programa que receba dez números inteiros. Calcule e mostre:
• A soma dos números primos
• A média dos números múltiplos de 3 que são maiores que 10
• A média dos números que são maiores ou iguais a 10 e menores ou iguais a 30'''

primos=somaM3=qtdM3=soma=qtd=0

for i in range(10):
    num=int(input("Insira um número: "))
    qtdDiv=0

    for j in range(1, num+1):
        if num%j==0:
            qtdDiv+=1
    if qtdDiv==2:
        primos+=num

    if num>10 and num%3==0:
        somaM3+=num
        qtdM3+=1
    if qtdM3==0:
        mediaM3=0
    else:
        mediaM3=somaM3/qtdM3

    if num>=10 and num<=30:
        soma+=num
        qtd+=1
    if qtd==0:
        media=0
    else:
        media=soma/qtd

print("=====================")
print("Soma dos Números Primos: ", primos)
print("Média dos multiplos de 3 maiores que 10: ", "%.2f" %mediaM3)
print("Média dos números entre 10 e 30: ", "%.2f" %media)
