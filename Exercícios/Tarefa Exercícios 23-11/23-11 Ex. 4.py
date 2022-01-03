'''Crie um programa que através de opções o usuário escolha o cálculo que desejar realizar.
1- verifica se o número é primo;
2 – verifica se o número é perfeito;
3 – calcula o fatorial do número.
Para cada cálculo deve ser criado uma função que recebe como parâmetro o número e retorna o resultado.
Número perfeito => a soma dos seus divisores exceto ele mesmo dá o próprio número'''

def primo(n):
    qtdDiv=0
    for i in range(1, n+1):
        if n%i==0:
            qtdDiv+=1
    if qtdDiv==2:
        print(f"O número {n} É PRIMO.")
    else:
        print(f"O número {n} NÃO É PRIMO.")

def perfeito(n):
    somaDiv=0
    for i in range(1, n):
        if n%i==0:
            somaDiv+=i
    if somaDiv==num:
        print(f"O número {n} É PERFEITO.")
    else:
        print(f"O número {n} NÃO É PERFEITO.")

def fatorial(n):
    fat=n
    for i in range(1, n):
        fat=fat*i
    print(f"O fatorial do número {n} é ", fat)

print("==========PROGRAMA PRINCIPAL===========")
num=int(input("\nInsira o número a ser calculado: "))
print("\n1- verifica se o número é primo;\n2 – verifica se o número é perfeito;\n3 – calcula o fatorial do número.")
opc=int(input("Escolha uma opção: "))

if opc==1:
    primo(num)
elif opc==2:
    perfeito(num)
elif opc==3:
    fatorial(num)
else:
    print("Opção Inválida!")