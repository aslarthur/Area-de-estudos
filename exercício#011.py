#Faça um programa que leia a largura e a altura da parede em metros, calcule a sua area, e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta 2 metros quadrados.

larg = float(input("Digite a largura da parede: "))
alt = float(input("Digite a altura da parede: "))
area = larg * alt
print (f"Sua parede tem a dimensão de {larg} x {alt} e sua area é de  {area}m²")
tinta = area / 2 
print (f"Para pintar essa parede você precisa de {tinta} litros de tinta")