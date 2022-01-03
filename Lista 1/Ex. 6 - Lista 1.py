'''6) Faça um programa que receba várias idades.
Para finalizar a entrada deve ser digitado idade zero ou negativa.
Calcule e mostre na tela:
• A quantidade de pessoas que tem idade entre 20 e 40 anos
• A maior idade
• A menor idade
• A média das idades'''

idade=int(input("Insira a idade: "))
maior_idade=idade
menor_idade=idade
qtd=soma=qtd_total=0
while idade>0:
    if idade>20 and idade<40:
        qtd+=1
        
    if idade>maior_idade:
        maior_idade=idade
        
    if idade<menor_idade:
        menor_idade=idade


    soma+=idade
    qtd_total+=1

    idade=int(input("Insira a idade: "))
    
media=soma/qtd_total
print("\n======================")
print("Quantidade de pessoas com idade entre 20 e 40 anos: ", qtd)
print("Maior idade: ", maior_idade)
print("Menor idade: ", menor_idade)
print("Média das idades: ", "%.2f" %media)

        
