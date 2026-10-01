# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.   A multa vai custar R$7,00 por cada Km acima do limite.

km = int(input("\nQuantos Km seu carro está? "))
if km > 80:
    calculo = km - 80
    multa = calculo * 7 
    print (f"\nA multa que você deve pagar é de R${multa}")
else:
    print ("\nVocê está dentro do limite de velocidade.\n")