'''1) Escreva um programa que leia um conjunto de 10 números inteiros.
Calcule e mostre:
a) o menor número
b) a soma dos números pares e maiores que 10
c) a quantidade de números ímpares
d) a média dos números maiores que 20'''

soma_par=qtd_impar=soma_maior_v=qtd_maior_v=0
for i in range (10):
    num=int(input("Insira o número: "))
    if i==0:
        menor_num=num
    elif num<menor_num:
        menor_num=num

    if num>10 and num%2==0:
        soma_par+=num

    if num%2!=0:
        qtd_impar+=1

    if num>20:
        soma_maior_v+=num
        qtd_maior_v+=1

media=soma_maior_v/qtd_maior_v

print("=======================")
print("Menor Número: ", menor_num)
print("Soma dos pares maiores que 10: ", soma_par)
print("Qtd números impares: ", qtd_impar)
print("Média dos maiores que 20: ", media)
