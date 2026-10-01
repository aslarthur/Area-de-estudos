#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

print ()
frase = str(input("Digite uma frase: "))
print ()
espaco = frase.replace (" ", "")
maiusculo = espaco.upper()
contagem = maiusculo.count("A")
direita = maiusculo.find ("A") + 1
esquerda = maiusculo.rfind ("A") + 1
total = len (frase.replace(" ", "")) 

print (f'Tem {contagem} letras "A" na palavra {frase}')
print ()
print (f'A letra "A" começa na {direita} palavra')
print ()
print (f'A letra "A" termina na {esquerda} letra.')
print ()
print (f'A frase "{frase}" tem {total} letras ao total')
print ()