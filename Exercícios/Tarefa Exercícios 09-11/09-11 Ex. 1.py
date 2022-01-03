'''Preencha uma lista com 5 nomes de alunos. Em seguida utilize o método upper()
para transformar em letra maiúscula todos os nomes armazenados na lista.
Faça uma rotina que procure por nomes nessa lista e substitua esse nome por outro.'''

alunos=[]
for i in range(5):
    alunos.append(str(input(f"Insira o nome do aluno {i+1}: ")))
for i in range(5):
    alunos[i] = alunos[i].upper()
    
print("Alunos:", alunos)

pesq=str(input("\nProcurar nome ou <fim>: "))
while pesq.upper() != 'FIM':
    if pesq.upper() in alunos:
        sub=str(input("Substituir nome por: "))
        idx=alunos.index(pesq.upper())
        alunos[idx]=alunos[idx].replace(pesq.upper(),sub.upper())
    else:
        print("Nome não encontrado!")
    print("Lista Atualizada: ", alunos)
    pesq=str(input("\nProcurar nome ou <fim>: "))
