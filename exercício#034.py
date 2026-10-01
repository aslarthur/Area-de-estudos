# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.   Para salarios superiores a R$1.250,00, calcule um aumento de 10%.   Para os inferiores ou iguais, o aumento é de 15%.  

salario = float(input("Digite quanto você recebe: "))
if salario <= 1250:
    novo_salario = salario + (salario * 15) / 100
    print ("Seu novo salario é de: {}".format(novo_salario))
else:
    salario_a_mais = salario + (salario * 10) / 100
    print ("Seu novo salario é de: {}".format(salario_a_mais))