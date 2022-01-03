'''.Crie uma função que receba um número inteiro como parâmetro e verifique se ele é primo ou não,
e exibindo uma mensagem dentro da função.'''

def primo(n):
    div=0
    for i in range(1, n+1):
        if n%i==0:
            div+=1
    if div==2:
        print("O número", n, "É PRIMO.")
    else:
        print("O número", n, "NÃO É PRIMO.")

num=int(input("Insira um número: "))
while num!=0:
    primo(num)
    num=int(input("\nInsira um número: "))    

