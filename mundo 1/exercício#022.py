# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas as letras minúsculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome

print ("________________________________________")
nome = input("Digite seu nome: ")
print ("________________________________________")
print ("Analisando seu nome...")
import time
time.sleep(5)

mai = nome.upper()
mi = nome.lower()
nor = nome.title()
l = len(nome.replace(" ", ""))
p = nome.split ()
print ("________________________________________")
print ("Em maiúsculo: ", mai)
print ("________________________________________")
print ("Em minúsculo: ", mi)
print ("________________________________________")
print ("Escrito normalmente: ", nor)
print ("________________________________________")
print ("Quantas letras ao todo: ", l)
print ("________________________________________")
print ("Quantas letras tem o primeiro nome: ",len (p [0]) )
print ("________________________________________")
