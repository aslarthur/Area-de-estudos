#Faça um programa que leia um 
# ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import radians, sin, cos, tan 
ângulo = float(input("Digite o algulo que você deseja: "))
sêno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print (f"O ângulo de {ângulo} tem o SENO de {sêno:.2f}")
print (f"O ângulo de {ângulo} tem o COSSENO de {cosseno:.2f}")
print (f"O ângulo de {ângulo} ten a TANGENTE de {tangente:.2f}")
