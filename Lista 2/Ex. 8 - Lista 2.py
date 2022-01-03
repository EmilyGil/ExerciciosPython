''' Escreva um programa que preencha uma lista com os nomes de 5 vendedores, preencha 
também outra lista com valor total das vendas de cada vendedor. Cada vendedor recebe 
10% de comissão sobre as vendas. Faça os seguintes cálculos e mostre os resultados na 
tela:
a. Uma listagem com o nome e o valor a receber de cada vendedor (total das 
vendas * 0.10)
b. O total (bruto) vendido pelos 5 vendedores
c. A média do total de vendas (valor bruto vendido por cada vendedor)
d. A quantidade de vendedores que venderam acima da média das vendas
e. O maior valor de comissão e o nome do vendedor que recebeu'''

import random
nomes=[]
vendas=[]
for i in range(5):
    nomes.append(str(input("\nInsira o nome do vendedor: ")))
    vendas.append(random.randint(0,500))
    print("Valor de vendas do vendedor: ", vendas[i])

print("\nVendedores: ", nomes)
print("Vendas: ", vendas)

total=sum(vendas)
media=(sum(vendas))/5
comissao=[]
qtd=0
for i in range(5):
    comissao.append(vendas[i]*0.1)
    if vendas[i]>media:
        qtd+=1
print("Comissao: ", comissao)

maiorCom=max(comissao)
idx=comissao.index(maiorCom)
print("\nTotal de vendas: ", total)
print("Média do total de vendas: ", media)
print("Qtd de vendedores com vendas acima da média: ", qtd)
print("Maior valor de comissão: ", maiorCom, "- Vendedor: ", nomes[idx])
