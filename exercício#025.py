#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input("Digite seu nome: "))

if "Silva" in nome:
    print (f"Olá, {nome}")
else:
    print (f"Opa, {nome}")