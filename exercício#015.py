#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dia = int(input("Digite por quantos dias você pegou o carro: "))
km = float(input("Digite quantos Km você rodou com o carro: "))
dia1 = dia * 60 + (km * 0.15)
print ("O valor total a pagar é R$ {:.2f}".format(dia1))

#60 dia. 0.15 por km