#Faça um algoritimo que leia um preço do produto e mostre seu novo preço, com 5% de desconto.

valor1 = float(input("Digite o valor do produto. R$ "))
valor2 = valor1 - (valor1 * 5 / 100)
print (f"O valor de R${valor1} com 5% de deconto fica apenas R${valor2}!" )