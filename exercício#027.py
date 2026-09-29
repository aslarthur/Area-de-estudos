#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

print ("___________________________")
nome = str(input("Digite seu nome: "))
print ("___________________________")

palavra = nome.split()
primeiro = palavra [0]
último = palavra [- 1]

print (primeiro)
print ("___________________________")
print (último)
print ("___________________________")

