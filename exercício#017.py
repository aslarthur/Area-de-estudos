#Faça um programa que leia o comprimento do cateto oposto 
#e do cateto adjacente de um triângulo retângulo, calcule e mostre 
# O comprimento da hipotenusa. 

co = float(input("Comprimento do cateto oposto: "))
# input() pede para o usuário digitar o comprimento.
# float() transforma o que foi digitado em número decimal.
# O valor é guardado na variável "co".

ca = float(input("Comprimento do cateto adjacente: "))
# Faz a mesma coisa, mas guarda o valor em "ca".

hi = (co ** 2 + ca ** 2) ** (1/2)
# Calcula a hipotenusa usando o Teorema de Pitágoras:
# hipotenusa² = cateto² + cateto²
# ** 2 significa "elevado ao quadrado".
# ** (1/2) significa "elevado a 1/2", ou seja, raiz quadrada.
# O resultado é guardado em "hi".

print("A hipotenusa vai medir: {:.2f}".format(hi))
# Mostra o resultado.
# {:.2f} significa mostrar o número com 2 casas decimais.

from math import hypot
# Importa a função "hypot" da biblioteca "math".
# hypot() já foi feita justamente para calcular a hipotenusa.

co = float(input("Comprimento do cateto oposto: "))
# Pede o primeiro cateto e transforma em número.

ca = float(input("Comprimento do cateto adjacente: "))
# Pede o segundo cateto e transforma em número.

hi = hypot(co, ca)
# hypot() recebe os dois catetos e calcula a hipotenusa.
# É equivalente a:
# (co ** 2 + ca ** 2) ** (1/2)

print("A hipotenusa vai medir: {:.2f}".format(hi))
# Mostra a hipotenusa com 2 casas decimais.