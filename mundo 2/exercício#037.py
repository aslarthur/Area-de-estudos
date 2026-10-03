# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

# 1 para binário
# 2 para octal
# 3 para hexadecimal
num = int(input("Digite um número inteiro: "))
print (f'''Escolha umas das bases para conversão: 
[ 1 ] Converter para \033[31mBINÁRIO\033[m
[ 2 ] Converter para \033[32mOCTAL\033[m
[ 3 ] Converter para \033[34mHEXADECIMAL\033[m''')
opção = int(input("Sua opção: "))
if opção == 1:
    print (f"{num} convertido para \033[31mBINÁRIO\033[m é igual a {bin(num)[2:]}")
elif opção == 2:
    print (f"{num} convertido para \033[32mOCTAL\033[m é igual a {oct(num)[2:]}")
elif opção == 3:
    print (f"{num} convertido para \033[34mHEXADECIMAL\033[m é igual a {hex(num)[2:]}")
else:
    print ("Opção inválida! Tente novamente")