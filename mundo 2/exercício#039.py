# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
idade = int(input("O seu ano de nascimento: "))
from datetime import date
ano = date.today().year
faltam = ano - idade

if faltam == 18:
    print ("É hora de se alistar ao serviço militar!")
elif faltam <17:
    print ("Você ainda vai precisar se alistar.")
elif faltam >= 19:
    print ("Já passou do tempo de se alistar!")

    