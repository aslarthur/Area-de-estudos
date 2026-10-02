# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

def linha():
    print ("-=" * 30)
linha()
emprestimo = float(input("Custa a casa? R$"))
linha()
salário = float(input("Quanto você recebe? R$"))
linha()
anos = int(input("Em quantos anos você vai pagar a casa? "))
linha()
valor_total = emprestimo / (anos * 12)
valor_final = salário * 30 / 100
if valor_total <= valor_final:
    print (f"Para pagar uma casa de R${emprestimo:.2f} em {anos} anos a prestação será de R${valor_total:.2f}!\nEmpréstimo pode ser CONCEDIDO!")
else:
    print (f"Para pagar uma casa de R${emprestimo:.2f} em {anos} anos a prestação será de R${valor_total:.2f}!\nEmpréstimo NEGADO")