'''Crie uma função que receba três valores, 'a', 'b' e 'c',
que são os coeficientes de uma equação do segundo grau e retorne o valor do delta,
que é dado por 'b² - 4ac’.'''

def delta(a, b, c):
    res=(pow(b, 2))-4*a*c
    return(res)

print("\n========PROGRAMA PRINCIPAL=========")
numA=int(input("Insira o coeficiente A: "))
numB=int(input("Insira o coeficiente B: "))
numC=int(input("Insira o coeficiente C: "))
valor_delta=delta(numA, numB, numC)
print("O valor de delta é: ", valor_delta)

