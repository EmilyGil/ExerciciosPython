'''2) Faça um programa que receba a idade e os respectivos
pesos de um número indeterminado de pessoas. Para finalizar
a entrada deve ser digitado idade zero ou negativa.
Calcule e mostre na tela: 
◦A maior idade
◦A quantidade de pessoas que pesam mais que 90 quilos.
◦A média de idade das pessoas que pesam menos que 50 quilos.'''

idade=int(input("Insira a idade: "))
cont=1
soma_idade=qtd_90=qtd_50=media=maior_idade=0

while idade>0:
    peso=float(input("Insira o peso: "))
    if cont==1:
        maior_idade=idade
    elif idade>maior_idade:
        maior_idade=idade

    if peso>90:
        qtd_90+=1

    if peso<50:
        soma_idade+=idade
        qtd_50+=1

    idade=int(input("Insira a idade: "))
    cont+=1
    
if qtd_50>0:
    media=soma_idade/qtd_50

print("=================")
print("Maior idade: ", maior_idade)
print("Qtd que pesa mais que 90 quilos: ", qtd_90)
print("Média de idade dos que pesam menos que 50 quilos: ", media)
        
