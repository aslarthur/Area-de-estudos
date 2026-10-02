#Faça um algoritimo que leia o salario de um funcionario e mostre seu nome salario, só que com 15% de aumento.

valor1 = float(input("Digite o valor: R$ "))
valor2 = valor1 + (valor1 *15 / 100 )
print (f"Você ganhou 15% de aumento! Aqui está seu novo salário: de R${valor1:.2f} para R${valor2:.2f}")