data = input("Você veio no dia da prova?\n1.Sim\n2.Não\nDigite o número da resposta: ")
if data == "1":
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    m = (n1 + n2) / 2
    print (f"Sua média foi: {m:.1f}")

    if m >= 6.0:
        print ("Sua média foi boa! PARABÉNS!")
    else:
        print ("Sua média foi ruim! ESTUDE MAIS")
else:
    print ("Por faltar no dia da prova, o estudante deve ficar de recuperação.")   
 
