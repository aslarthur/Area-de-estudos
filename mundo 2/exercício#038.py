# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
def linha():
    print ("-=" * 50)
linha()
n1 = int(input(f"Digite o \033[32mprimeiro\033[m valor: "))
linha()
n2 = int(input("Digite o \033[33msegundo\033[m valor: "))
linha()
if n1 > n2:
    print (f"\033[32m{n1}\033[m é maior que \033[33m{n2}\033[m.")
    linha()
elif n2 > n1:
    print (f"\033[32m{n2}\033[m é maior que \033[33m{n1}\033[m.")
    linha()
else:
    print (f"\033[32m{n1}\033[m é igual a \033[32m{n2}\033[m.")
    linha()