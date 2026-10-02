# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER
idade = int(input("Digite sua idade: "))
if idade <=9:
    print ("MIRIM")
elif idade == 10 or idade <= 14:
    print ("INFANTIL")
elif idade == 15 or idade <= 19:
    print ("JÚNIOR")
elif idade == 20:
    print ("SÊNIOR")
else:
    print ("MASTER")