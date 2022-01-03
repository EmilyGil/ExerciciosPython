'''3) Faça um programa que receba a idade, altura e o peso de 10 pessoas, calcule e mostre:
a) A quantidade de pessoas com idade superior a 50 anos e que pesam mais que 90 quilos;
b) A média do peso das pessoas com idade entre 30 e 50 anos (inclusive);
c) A média da altura de todas pessoas;
d) A media de altura da pessoas com idade entre 15 e 25 anos (inclusive).'''

qtd_total=qtd_a=qtd_b=qtd_d=soma_alt=soma_b=soma_d=0
for i in range(10):
    idade=int(input("\nInsira a idade: "))
    altura=float(input("Insira a altura: "))
    peso=float(input("Insira o peso: "))

    qtd_total+=1
    soma_alt+=altura

    if idade>50 and peso>90:
        qtd_a+=1

    if idade>=30 and idade<=50:
        soma_b+=peso
        qtd_b+=1

    if idade>=15 and idade<=25:
        soma_d+=altura
        qtd_d+=1

if qtd_b>0:
    media_b=soma_b/qtd_b
else:
    media_b=0
    
media_alt=soma_alt/qtd_total

if qtd_d>0:
    media_d=soma_d/qtd_d
else:
    media_d=0
    
print("\na) A qtd com idade superior a 50 anos e mais de 90 quilos: ", qtd_a)
print("b) A média do peso das pessoas com idade entre 30 e 50 anos: ", "%.2f" %media_b)
print("c) A média da altura de todas pessoas: ", "%.2f" %media_alt)
print("d) A media de altura da pessoas com idade entre 15 e 25 anos: ", "%.2f" %media_d)
