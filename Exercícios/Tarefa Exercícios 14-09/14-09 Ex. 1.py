'''1.Faça um programa que preencha uma lista com 10 nomes diferentes,
uma segunda lista com as idades e uma terceira lista com peso.
Depois permita fazer uma pesquisa se um determinado nome existe armazenado
na lista, se existir deve ser impresso na tela o nome, idade e o peso,
a pesquisa deve ser feita até que seja digitado FIM no nome a ser pesquisado
na lista'''

from random import randint, uniform

nomes=[]
idades=[]
pesos=[]

for i in range(10):
    nomes.append(str(input("\nNome: ")))
    idades.append(randint(10, 80))
    print("Idade: ", idades[i])
    pesos.append(round(uniform(50, 100),2))
    print("Peso: %.2f" %pesos[i])

print("\nNomes: ", nomes)
print("Idades: ", idades)
print("Pesos: ", pesos)

nome=str(input("\nConsultar nome: "))
while nome.upper() != 'FIM':
    if nome in nomes:
        idx=nomes.index(nome)
        print(nomes[idx], "tem", idades[idx], "anos e pesa", pesos[idx], "quilos")
    else:
        print("Nome não encontrado")

    nome=str(input("\nConsultar nome: "))
