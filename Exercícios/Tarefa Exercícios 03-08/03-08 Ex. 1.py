'''
1) Faça um programa que receba a idade, e conforme a faixa etária exiba a mensagem se é criança, adolescente, adulto ou idoso.

-De 0 a 12 anos – criança
-De 13 a 17 anos – adolescente
-De 18 a 59  anos– adulto
-De 60 anos em diante - idoso
'''

idade=int(input("Insira a idade: "))

if idade>=0 and idade<=12:
    print("CRIANÇA")
elif idade>=13 and idade<=17:
    print("ADOLESCENTE")
elif idade>=18 and idade<=59:
    print("ADULTO")
elif idade>=60:
    print("IDOSO")
else:
    print("Idade INVÁLIDA!!")
