#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print ("-=-" * 20)
print ("Analisador de Triângulos")
print ("-=-" * 20)
r1 = float(input("Digite o comprimento da primeira reta: "))
print ("-=-" * 20)
r2 = float(input("Digite o comprimento da segunda reta: "))
print ("-=-" * 20)
r3 = float(input("Digite o comprimento da terceira reta: "))
print ("-=-" * 20)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print ("O triangulo PODE ser formado.")
    print ("-=-" * 20)
else:
    print ("O triangulo NÃO pode ser formado.")
    print ("-=-" * 20)