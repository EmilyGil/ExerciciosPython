'''Escreva uma função que receba como parâmetro a nota de um estudante,
converte o valor de nota para um conceito (A, B, C, D, E e F). Imprima o resultado dentro da função.'''

def conversor(nota):
    if nota<=10 and nota>=9:
        conc='A'
    elif nota<9 and nota>=8:
        conc='B'
    elif nota<8 and nota>=7:
        conc='C'
    elif nota<7 and nota>=6:
        conc='D'
    elif nota<6 and nota>=5:
        conc='E'
    elif nota<5 and nota>=0:
        conc='F'
    else:
        conc='Inválido'
        print("Nota inválida!")

    print("Conceito final: ", conc)


print("\n======CONVERSOR DE NOTA PARA CONCEITO========")
num=float(input("Insira a nota a ser convertida: "))
conversor(num)