'''(Exercício 1) Uma empresa de ônibus precisa de um sistema para facilitar a venda de passagens.
O ônibus possui 40 lugares e o usuário pode escolher a poltrona informando um número de 1 a 40,
se a poltrona estiver ocupada deverá ser exibido uma mensagem informando que a poltrona já está ocupada,
 caso contrário a poltrona deve ser reservada. O sistema deve ser encerrado quando for digitado zero no
  número da poltrona. No final deve ser exibido na tela:
◦a quantidade de poltronas ocupadas
◦a quantidade de poltronas livres
◦Obs: deve ser usado listas para resolver este problema'''


polt=[0]*41
num=int(input("Informe o número da poltrona reservada entre 1 e 40: "))
while num != 0:
    if num < 0 or num > 40:
        print("Digite uma poltrona válida (1-40)")
    else:
        if polt[num] == 0:
            polt[num]=1
            print("Poltrona", num,"reservada com sucesso")
        else:
            print("Poltrono", num,"já reservada, escolha outra")
    num = int(input("Informe o número da poltrona reservada entre 1 e 40: "))

ocup = 0
for i in range(1, 41):
    if polt[i] == 1:
        ocup+=1
livre=40-ocup


print("Quantidade de poltronas ocupadas: ", ocup)
print("Quantidade de poltronas livres: ", livre)