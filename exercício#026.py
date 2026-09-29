#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

print ("________________________________")
frase = str(input("Digite uma frase: "))
print ("________________________________")

contagem = frase.upper()
conta = contagem.count("A")
esquerda = contagem.find("A")
direita = contagem.rfind("A")

print (f'A frase tem {conta} letras "A"!')
print ("_______________________________")
print (f'A primeira letra "A" começa na palavra {esquerda}')
print ("_______________________________")
print (f'A última letra "A" termina na {direita} palavra.')
print ("_______________________________")