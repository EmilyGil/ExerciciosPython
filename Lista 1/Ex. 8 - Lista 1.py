'''
8) Em um campeonato de futebol existem cinco times e cada um possui onze jogadores. Faça 
um programa que receba a idade, o peso e a altura de cada um dos jogadores, calcule e 
mostre:
• A quantidade de jogadores com idade inferior a 18 anos
• A média das idades dos jogadores de cada time
• A média das alturas de todos os jogadores do campeonato
• A percentagem de jogadores com mais de 80 quilos entre todos os jogadores 
do campeonato
'''

from random import randint, uniform
menor=0
somaIdade1=0
somaIdade2=0
somaIdade3=0
somaIdade4=0
somaIdade5=0
somaAltura=0
qtdPeso=0
print("=======TIME 1========")
for i in range(11):
    idade1=int(randint(10, 50))
    print("\nIdade do jogador ", i+1, ": ", idade1)
    peso1=float(uniform(50, 100))
    print("Peso do jogador ", i+1, ": ", "%.2f" %peso1)
    altura1=float(uniform(1.5, 2))
    print("Altura do jogador ", i+1, ": ", "%.2f" %altura1)
    
    if idade1<18:
        menor+=1
    somaIdade1+=idade1
    somaAltura+=altura1
    if peso1>80:
        qtdPeso+=1
        
print("\n=======TIME 2========")
for j in range(11):
    idade2=int(randint(10, 50))
    print("\nIdade do jogador ", j+1, ": ", idade2)
    peso2=float(uniform(50, 100))
    print("Peso do jogador ", j+1, ": ", "%.2f" %peso2)
    altura2=float(uniform(1.5, 2))
    print("Altura do jogador ", j+1, ": ", "%.2f" %altura2)
    if idade2<18:
        menor+=1
    somaIdade2+=idade2
    somaAltura+=altura2
    if peso1>80:
        qtdPeso+=1

print("\n=======TIME 3========")
for k in range(11):
    idade3=int(randint(10, 50))
    print("\nIdade do jogador ", k+1, ": ", idade3)
    peso3=float(uniform(50, 100))
    print("Peso do jogador ", k+1, ": ", "%.2f" %peso3)
    altura3=float(uniform(1.5, 2))
    print("Altura do jogador ", k+1, ": ", "%.2f" %altura3)
    if idade3<18:
        menor+=1
    somaIdade3+=idade3
    somaAltura+=altura3
    if peso3>80:
        qtdPeso+=1

print("\n=======TIME 4========")
for l in range(11):
    idade4=int(randint(10, 50))
    print("\nIdade do jogador ", l+1, ": ", idade4)
    peso4=float(uniform(50, 100))
    print("Peso do jogador ", l+1, ": ", "%.2f" %peso4)
    altura4=float(uniform(1.5, 2))
    print("Altura do jogador ", l+1, ": ", "%.2f" %altura4)
    if idade4<18:
        menor+=1
    somaIdade4+=idade4
    somaAltura+=altura4
    if peso4>80:
        qtdPeso+=1

print("\n=======TIME 5========")
for m in range(11):
    idade5=int(randint(10, 50))
    print("\nIdade do jogador ", m+1, ": ", idade5)
    peso5=float(uniform(50, 100))
    print("Peso do jogador ", m+1, ": ", "%.2f" %peso5)
    altura5=float(uniform(1.5, 2))
    print("Altura do jogador ", m+1, ": ", "%.2f" %altura5)
    if idade5<18:
        menor+=1
    somaIdade5+=idade5
    somaAltura+=altura5
    if peso5>80:
        qtdPeso+=1
        
mediaIdade1=somaIdade1/11
mediaIdade2=somaIdade2/11
mediaIdade3=somaIdade3/11
mediaIdade4=somaIdade4/11
mediaIdade5=somaIdade5/11
mediaAltura=somaAltura/55
porc=(qtdPeso*100)/55

print("\n===========================")
print("Qtd de jogadores com idade inferior a 18: ", menor)
print("Média das idades dos jogadores do time 1: ", "%.2f" %mediaIdade1)
print("Média das idades dos jogadores do time 2: ", "%.2f" %mediaIdade2)
print("Média das idades dos jogadores do time 3: ", "%.2f" %mediaIdade3)
print("Média das idades dos jogadores do time 4: ", "%.2f" %mediaIdade4)
print("Média das idades dos jogadores do time 5: ", "%.2f" %mediaIdade5)
print("Média de todas as alturas: ", "%.2f" %mediaAltura)
print("Porcentagem de jogadores com mais de 80 quilos: ", "%.2f" %porc, "%")
