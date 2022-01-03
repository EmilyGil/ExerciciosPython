from random import randint
nome=[]
idade=[]
peso=[]

for i in range(5):
    nome.append(str(input("Nome: ")))
    idade.append(randint(1, 120))
    peso.append(randint(20, 90))

print(nome)
print(idade)
print(peso)

pesq=str(input("Digite um nome para ser buscado ou FIM: "))

while(pesq.upper() != "FIM"):
    if pesq in nome:
        idx=nome.index(pesq)
        print("Nome: ", nome[idx], " - Idade: ", idade[idx], " - Peso: ", peso[idx])
    else:
        print("O nome: ", pesq, " não foi encontrado!!")

    pesq=str(input("Digite um nome para ser buscado ou FIM: "))
