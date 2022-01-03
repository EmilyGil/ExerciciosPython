'''5) Faça um programa que preencha uma lista com os nomes de 5 produtos, e outra lista com 
o valor dos produtos. Calcule e mostre:
a. a quantidade de produtos que o valor é abaixo de 10 reais;
b. a média dos valores dos produtos;
c. a quantidade de produtos que valor acima da média;
d. a maior valor e o nome do produto;
e. faça uma listagem que imprima na tela (Nome Vlr do produto)'''

produtos=[]
valores=[]
qtdMenor=qtdAcimaM=mediaVal=0
for i in range(5):
    produtos.append(str(input("\nCadastre um produto: ")))
    valores.append(float(input("Valor do produto: ")))
mediaVal=(sum(valores)/len(valores))
for j in range(5):
    if (valores[j]<10):
        qtdMenor+=1
    if (valores[j]>mediaVal):
        qtdAcimaM+=1
maiorVal=max(valores)
idxMaior=valores.index(maiorVal)

print("\n=======PRODUTOS CADASTRADOS========")
for k in range(5):
    print(produtos[k], "= R$", valores[k])
print("\nA)Qtd de produtos com valor abaixo de 10 reais: ", qtdMenor)
print("B)Média dos valores dos produtos: R$ %.2f" %mediaVal)
print("C)Qtd de produtos com valor acima da média: ", qtdAcimaM)
print("D)Produto de maior valor: ", produtos[idxMaior], "= R$", maiorVal)
