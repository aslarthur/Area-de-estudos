# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.   

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

número = [0, 1, 2, 3, 4, 5,]
while True: 
    n = int(input("\nDigite um número: "))
    import random
    computador = random.choice (número)
    if n == computador:
        print ("\nVocê ganhou!")
    else:
        print ("\nO computador ganhou!")
    print ("\nQuer continuar?")
    print ("\n1. Sim")
    print ("\n2. Não")
    sn = input("\nDigite o número da resposta: ")
    if sn == "1":
        print ("\nÓtimo!")
        continue
    else:
        print ("\nTudo bem. Até a próxima!")
        break