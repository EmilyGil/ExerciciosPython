'''Crie uma função que receba dois números inteiros por parâmetro e
retorne a soma dos N números inteiros existentes entre esses dois números(inclusive).
Imprima o resultado no programa principal.'''

def soma(num1, num2):
    total=0
    for i in range(num1, num2+1):
        total+=i
    return(total)

print("====Programa principal=====")
n1=int(input("Insira o número 1: "))
n2=int(input("Insira o número 2: "))
res=soma(n1, n2)
print("A soma dos N números entre", n1, "e", n2, "é: ", res)
        
