#Escreva um programa que exiba um valor em metros e exiba convertido em centímetros e milímetros.

medida = float(input("Digite uma distancia em metros: "))
cm = medida * 100
mm = medida * 1000
print ("A medida de {}m corresponde a {:.0f} E a {:.0f}mm".format (medida, cm, mm)) 
