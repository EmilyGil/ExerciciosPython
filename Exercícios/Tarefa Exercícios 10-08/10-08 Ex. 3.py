'''3) Faça um programa que receba a idade e as alturas de 10 atletas.
Calcule e mostre na tela: 
◦A maior idade
◦A menor idade
◦A média das alturas
◦A maior altura'''

media=soma_alt=0
for i in range (10):
    idade=int(input("Insira a idade: "))
    altura=float(input("Insira a altura: "))
    if i==0:
        maior_idade=idade
        menor_idade=idade
        maior_alt=altura
    elif idade>maior_idade:
        maior_idade=idade
    elif idade<menor_idade:
        menor_idade=idade
        
    if altura>maior_alt:
        maior_alt=altura

    soma_alt+=altura

media=soma_alt/10
print("=================")
print("Maior idade: ", maior_idade)
print("Menor idade: ", menor_idade)
print("Média das alturas: ", "%.2f" %media)
print("Maior altura: ", maior_alt)
