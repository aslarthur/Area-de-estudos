# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

km = int(input("\nDigite quantos km a viagem tem: "))
if km <= 200:
    preço = km * 0.50
    print (f"\nVocê tem que pagar R${preço:.2f}")
else:
    novo_preço = km * 0.45
    print (f"\nVocê tem que pagar R${novo_preço:.2f}")
print (f"\nVocê está prestes a começar uma viagem de {km}Km")