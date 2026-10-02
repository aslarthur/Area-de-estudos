# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
produto = str(input("Digite o produto: "))
preço = float(input("Digite o valor do produto: "))
valor = str(input(f"O valor final é de R${preço:.2f}. Formas de pagameto:\n1.À vista no dinheiro/cheque: 10 % de desconto\n2.À vista no cartão: 5 % de desconto\n3.Em até 2x no cartão: preço normal\n4.3x ou mais no cartão: 20 % de juros\nDigite o número da forma de pagamento: "))
if valor == "1":
    preço = preço - (preço * 10 / 100 )
    print (f"O valor final é de R${preço:.2f}")
elif valor == "2":
    preço = preço - (preço * 5 / 100)
    print (f"O valor final é de R${preço}")
elif valor == "3":
    print (f"O valor final é de R${preço}")
elif valor == "4":
    valor = valor * (valor * 20 / 100)
    print (f"O valor final é de R${preço}")