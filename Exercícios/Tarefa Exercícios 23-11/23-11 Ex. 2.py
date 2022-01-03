'''A prefeitura de uma cidade fez uma pesquisa entre 10 habitantes, coletando dados sobre o salário e número de filhos.
Calcule:
◦Faça uma função que receba como parâmetro uma lista com os salários e retorne a média de salário da população.
◦Faça uma função que receba como parâmetro uma lista com o número de filhos e retorne a média do número de filhos.
◦Obs: Exiba no programa principal os resultados.'''
import random

def media_salarios(vetor):
    soma=sum(vetor)
    qtd=len(vetor)
    media=soma/qtd
    return(media)

def media_filhos(vetor):
    soma=sum(vetor)
    qtd=len(vetor)
    media=soma/qtd
    return(media)

print("=========PROGRAMA PRINCIPAL==========")
salarios=[]
filhos=[]
for i in range(10):
    salarios.append(random.randint(500, 5000))
    filhos.append(random.randint(0, 5))

print("Salários: ", salarios)
print("Qtd de filhos: ", filhos)

mediaSal=media_salarios(salarios)
mediaFil=media_filhos(filhos)

print("\nMédia de salário da população: R$ %.2f" %mediaSal)
print("Média do número de filhos: %.2f" %mediaFil)