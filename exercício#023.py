#Faça um programa que leia um número de o a 9999 e mostre na tela cada um dos dígitos separados
#Ex: Digite um número: 1834

#milhar:1
#centena: 8
#dezena: 3
#unidade: 4

num = int(input("Digite um número: "))
m = num // 1000
c = (num // 100) % 10
d = (num // 10) % 10
u = num % 10
print (f"Milhar: {m}")
print (f"Centena: {c}")
print (f"Dezena: {d}")
print (f"Unidade: {u}")