#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input("Digite seu nome: "))
ola = nome.upper()
if "SILVA" in ola:
    print (f"Olá, {nome}")
else:
    print (f"Opa, {nome}")