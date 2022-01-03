''' 3) Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e 
sua opinião em relação ao filme (3- ótimo;2- bom;1-regular)
Faça um programa que receba a idade e a opinião de um número indeterminado de 
pessoas. Para finalizar a entrada deve ser digitado uma idade negativa ou zero. Calcule e 
mostre:
• A quantidade de pessoas que responderam ótimo
• A quantidade de pessoas que responderam regular
• A quantidade de pessoas que responderam bom
• A média das idades das pessoas'''

qtdRegular=qtdBom=qtdOtimo=soma=qtdIdade=0

idade=int(input("Insira sua idade: "))

while idade>0:
    opiniao=int(input("Digite sua avaliação sobre o filme: \n 1 - REGULAR \n 2 - BOM \n 3 - ÓTIMO \n"))
    if opiniao==1:
        qtdRegular+=1
    elif opiniao==2:
        qtdBom+=1
    elif opiniao==3:
        qtdOtimo+=1
    else:
        print("Avaliação Inválida!")

    qtdIdade+=1
    soma+=idade
    idade=int(input("Insira sua idade: "))

media=soma/qtdIdade

print("=======RESULTADOS=========")
print("Qtd de avaliações ÓTIMO: ", qtdOtimo)
print("Qtd de avaliações REGULAR: ", qtdRegular)
print("Qtd de avaliações BOM: ", qtdBom)
print("Média das idades: ", "%.2f" %media)

        
