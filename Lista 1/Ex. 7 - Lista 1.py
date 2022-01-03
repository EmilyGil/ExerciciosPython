'''7) Faça um programa que calcule e mostre na tela a tabuada de 1 a 10.'''

'''for j in range (1, 11):
    print("\n========= TABUADA DO ", j, " ==========")
    for i in range (1, 11):
        r=i*j
        print(i, "x", j, "=", r)'''

tab=int(input("Insira a tabuada que deseja visualizar: "))
for i in range (1, 11):
    r=i*tab
    print(i, "x", tab, "=", r)
