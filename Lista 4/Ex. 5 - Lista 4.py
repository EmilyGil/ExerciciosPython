'''Escreva uma função que receba como parâmetro uma lista com 10 nomes
e um nome para pesquisa. Essa função deverá realizar uma busca do nome na lista,
retornando TRUE se encontrar ou FALSE se não encontrar'''


def buscar(lista):
    print("\nLista de nomes: ", lista)
    pesq=str(input("\nBuscar nome: "))
    if pesq.upper() in lista:
        res='TRUE'
    else:
        res='FALSE'
    print(res)

nomes=[]
for i in range(10):
    nome=str(input(f"Nome {i+1}: "))
    nomes.append(nome.upper())

buscar(nomes)
