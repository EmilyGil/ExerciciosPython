''' media=soma=qtd=0
    cont=1
    while cont<=5:
        idade=int(input("Digite a idade:"))
        altura=float(input("Digite a altura"))
        soma_alt+=altura
        soma+=idade
        if idade>30:
            qtd+=1

        cont+=1

    media=soma_alt/5
    print("A soma das idades: ", soma)
    print("A média das alturas: ", media)
    print("Qtd de pessoas com mais de 30 anos: ", qts)

'''

i=0
soma_alt=0
soma_idade=0
qtd=0
for i in range (5):
    idade=int(input("Insira a idade: "))
    altura=float(input("insira a altura: "))
    print("================")
    soma_alt=altura+soma_alt
    soma_idade=idade+soma_idade
    if idade>30:
        qtd=qtd+1

media=soma_alt/5
print("==================")
print("A média das alturas é: ", "%.2f" %media)
print("A soma das idades é: ", soma_idade)
print("A qtd de pessoas com idade superior a 30 anos é: ", qtd)
