# Cria um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
# Ex:
# Digite um número: 6.127
# O número 6.127 tem a parte Inteira 6.

num = float(input("Digite um número: "))
print ("O valor digitado foi {}.\nE sua porção inteira é {}.".format (num, int(num)))

#______________________________________________________________________________________________

num = float(input("Digite um número: "))
num1 = int(num)
print ("O valor digitado foi {}.\nE sua porção inteira é {}.".format (num,num1))

#______________________________________________________________________________________________

from math import trunc 

num = float(input("Digite um número: "))
print ("O valor digitado foi {}.\nE sua porção inteira é {}".format (num, trunc(num)))