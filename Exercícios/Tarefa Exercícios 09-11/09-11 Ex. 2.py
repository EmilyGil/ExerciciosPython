'''Faça um programa que peça como entrada 2 palavras, em seguida junte essas duas palavras
em uma string e depois faça uma busca de uma palavra ou sílaba nessa string usando find().'''

continuar=str(input("Deseja iniciar? S ou N\n"))
while continuar=='s' or continuar=='S':
    p1=str(input("Digite uma palavra: "))
    p2=str(input("Digite outra palavra: "))

    palavra=p1.upper()+p2.upper()

    print("\nPalavra formada: ", palavra)

    busca=str(input("\nBuscar palavra ou sílaba: "))
    res=palavra.find(busca.upper())
    if res > 0:
        print(f"Busca encontrada na palavra! Índice: {res}")
    else:
        print("Nenhum resultado encontrado!")
    continuar=str(input("\nDeseja continuar? S ou N\n"))
