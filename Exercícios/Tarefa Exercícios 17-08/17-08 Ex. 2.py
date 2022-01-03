'''2) Faça um programa que receba vários números, calcule e mostre:
◦A soma dos números digitados
◦A média dos números digitados
◦O maior número digitado
◦A média dos números múltiplos de 3
◦A quantidade números primos
◦A quantidade de números múltiplos de 5
Finalize a entrada digitando o número zero ou negativo
'''

soma=qtd=mult3_soma=mult3_qtd=qtd_primo=mult5_qtd=0

num=int(input("Insira o número: "))

maior=num
while num>0:
    qtd_div=0
    soma+=num
    qtd+=1
    
    if num>maior:
        maior=num
        
    if num%3==0:
        mult3_soma+=num
        mult3_qtd+=1

    for i in range(1, num+1):
        if num%i==0:
            qtd_div+=1
            
    if qtd_div==2:
        qtd_primo+=1

    if num%5==0:
        mult5_qtd+=1

    num=int(input("Insira o número: "))

media=soma/qtd

if mult3_qtd>0:
    mult3_media=mult3_soma/mult3_qtd
else:
    mult3_media=0

print("\n◦A soma dos números digitados: ", soma)
print("◦A média dos números digitados: ", media)
print("◦O maior número digitado: ", maior)
print("◦A média dos números múltiplos de 3: ", mult3_media)
print("◦A quantidade números primos: ", qtd_primo)
print("◦A quantidade de números múltiplos de 5: ", mult5_qtd)

    
