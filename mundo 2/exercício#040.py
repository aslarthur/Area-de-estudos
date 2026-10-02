# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota = float(input("Digite quanto você tirou: "))
if nota < 5:
    print ("REPROVADO")
elif nota >=7:
    print ("APROVADO!")
else:
    print ("RECUPERAÇÃO")
