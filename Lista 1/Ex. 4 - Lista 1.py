'''4) Faça um programa que receba dez números inteiros. Calcule e mostre:
• A quantidade de números primos
• A soma dos números múltiplos de 3
• A média dos pares que são maiores que 20
'''

primos=soma_mult=soma_par=qtd_par=0

for i in range(10):
    num=int(input("Insira o número: "))
    qtd_div=0
    for j in range(1, num+1):
        if num%j==0:
            qtd_div+=1

    if qtd_div==2:
        primos+=1

    if num%3==0:
        soma_mult+=num

    if num%2==0 and num>20:
        soma_par+=num
        qtd_par+=1

if qtd_par==0:
    media_par=0
else:
    media_par=soma_par/qtd_par

print("\n======RESULTADOS========")
print("Qtd de números primos: ", primos)
print("Soma dos múltiplos de 3: ", soma_mult)
print("Média dos números pares maiores que 20: ", "%.2f" %media_par)
