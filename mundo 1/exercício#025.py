#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input("Digite seu nome: ")).strip()      
ola = nome.upper()
if "SILVA" in ola:
    print ('Seu nome tem "Silva"!')
else:
    print ('Seu nome não tem "Silva".')