'''Crie uma função que receba 1 número inteiro como parâmetro e verifique se ele é perfeito,
ou seja, se a soma dos seus divisores exceto ele mesmo dá o próprio número, a mensagem se o número
é perfeito ou não deve ser mostrada no programa principal.'''

def perfeito(num):
    somaDiv=0
    for i in range(1, num):
        if num%i==0:
            somaDiv+=i
    return(somaDiv)

print("\n=========PROGRAMA PRINCIPAL==========")
n=int(input("Insira um número inteiro: "))
res=perfeito(n)
if res==n:
    print("O número", n, "é PERFEITO")
else:
    print("O número", n, "NÃO É PERFEITO")



