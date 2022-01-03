'''Faça um programa que preencha uma lista com 10 cores diferentes. Depois permita fazer 
uma pesquisa se uma determinada cor existe armazenada na lista, se existir deve ser 
impresso na tela a cor e em qual posição (índice) esta cor está armazenada. A pesquisa 
deve ser feita até que seja digitado FIM na cor a ser pesquisada na lista.'''

cores=[]
for i in range(10):
    cores.append(str(input("Cor: ")))
print("\nCores: ", cores)
pesq=str(input("\nDigite a cor a ser consultada ou FIM: "))
while pesq.upper() != 'FIM':
    if pesq in cores:
        idx=cores.index(pesq)
        print("-> Cor:", cores[idx], "- Índice:", idx)
    else:
        print("\nCor não encontrada na lista!")

    pesq=str(input("\nDigite a cor a ser consultada ou FIM: "))
