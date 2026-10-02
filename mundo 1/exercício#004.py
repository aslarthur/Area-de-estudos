#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

a = input("Digite algo: ")
print ("O tipo primitivo desse valor é: ", type (a))
print ("É maiúscula?",a.isupper())
print ("É minuscula?", a.islower())
print ("Tem espaço?", a.isspace())
print ("Tem algum número?", a.isnumeric())
print ("Tem alguma letra?", a.isalpha())
print ("Tem letra e número?", a.isalnum())
print ("Tem algum acento?", a.isascii())

