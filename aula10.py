data = input("\nVocê veio no dia da prova?\n1.Sim\n2.Não\nDigite o número da resposta: ")
if data == "1":
    n1 = float(input("\nDigite a primeira nota: "))
    n2 = float(input("\nDigite a segunda nota: "))
    m = (n1 + n2) / 2
    print (f"\nSua média foi: {m:.1f}\n")
print ("Sua nota foi boa! PARABÉNS!" if m >= 6 else "Sua nota foi ruim. ESTUDE MAIS!")
