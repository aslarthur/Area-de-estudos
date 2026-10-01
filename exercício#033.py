# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.   Para salários superiores a R$1.250,00, calcule um aumento de 10%.   Para os inferiores ou iguais, o aumento é de 15%.
salário = float(input("Digite o salário do funcionário: R$"))
if salário <= 1.250:
    aumento15 = salário + (salário * 15 / 100)
    print (f"Seu NOVO salário é de R${aumento15:.2f}")
else:
    aumento10 = salário + (salário * 10 / 100 )
    print (f"Seu NOVO salário é de R${aumento10:.2f}")