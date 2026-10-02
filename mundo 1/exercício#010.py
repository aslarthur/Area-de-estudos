#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.

valor1 = float(input("Digite quanto dinheiro você tem! R$ "))
dolar = valor1 / 5.17
euro = valor1 / 5.97
print (f"Com {valor1:.2f} você pode comprar US${dolar:.3f}! ")
print (f"E com {valor1:.2f} você pode comprar:  €{euro:.2f} ")