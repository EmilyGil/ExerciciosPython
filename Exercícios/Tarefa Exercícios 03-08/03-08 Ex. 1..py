soma=0
inf=0
for i in range (10):
    n=int(input("Insira um número: "))
    if n%2==0 :
        soma=soma+n
    if n<10:
        inf=inf+1
        
print("=============================")
print("A soma dos número pares é: ", soma)
print("A quantidade de números inferiores a 10 é: ", inf)
