'''Faça um programa que, leia uma matriz 5x2 com os números de telefones dos clientes,
as linhas representam os clientes, as colunas representam os telefones.
E uma lista de 5 elementos com os nomes dos clientes. Depois de preenchidos a lista e a matriz,
deverá ser feito uma busca pelo nome do cliente, se o nome existir, deverá ser mostrado na tela, os telefones desse cliente.'''
import random
mat=[]
clientes=[]

for i in range(5):
    linha=[]
    for j in range(2):
        linha.append(random.randint(990000000, 999999999))
    mat.append(linha)
print("Telefones cadastrados:")
for i in range(5):
    print(mat[i])

print("\n")
for k in range(5):
    cliente=str(input(f"Cliente {k+1}: "))
    clientes.append(cliente.upper())

print("\nClientes:", clientes)

print("\n========CONSULTAR TELEFONE DE CLIENTE==========")
print("Caso deseje encerrar a operação digite <fim>\n")
pesq=(input("Digite o nome do cliente: "))
pesq=pesq.upper()
while pesq != 'FIM':
    if pesq in clientes:
        idx=clientes.index(pesq)
        print("Telefone 1:", mat[idx][0])
        print("Telefone 2:", mat[idx][1])
    else:
        print("Cliente não encontrado!")
    pesq=str(input("\nDigite o nome do cliente: "))
    pesq=pesq.upper()
    
