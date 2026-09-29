#Faça um programa que leia um número de o a 9999 e mostre na tela cada um dos dígitos separados
#Ex: Digite um número: 1834

#milhar:1
#centena: 8
#dezena: 3
#unidade: 4

num = int(input("Digite um número: "))
print ("Calculando...")

n = str(num)
import time 
time.sleep(3)

print ("Unidade: {}".format (n [3]))
print ("Dezena: {}".format (n [2]))
print ("Centena: {}".format (n [1]))
print ("Milhar: {}".format (n [0]))
