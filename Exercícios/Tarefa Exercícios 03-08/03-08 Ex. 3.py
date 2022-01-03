'''
3) Escreva um programa que leia 10 notas e mostre na tela
a média dos alunos e a quantidade de alunos que tiveram nota inferior a 6
'''

soma=0
qtd=0
for i in range(10):
    nota=float(input("Insira nota do aluno: "))
    soma=soma+nota
    if nota<6:
        qtd=qtd+1
media=soma/10
print("=========================")
print("Média dos alunos: ", media)
print("Quantidade de alunos com nota inferior a 6: ", qtd)
