linha = "-=" * 30
print (linha)
mensagem = f'''Digite alguma dessas cores: 
{linha}
Branco
{linha}
Vermelho
{linha}
Verde
{linha}
Amarelo
{linha}
Roxo
{linha}
Azul
{linha}
Azul Claro
{linha}
Cinza
{linha} 
Digite a cor aqui: '''
cor = input(mensagem).strip()
print (linha)
nova_cor = cor.upper()

if nova_cor == "BRANCO":
    print (f"\033[1;4;37m{nova_cor}\033[m")
elif nova_cor == "VERMELHO":
    print (f"\033[1;4;31m{nova_cor}\033[m")
elif nova_cor == "VERDE":
    print (f"\033[1;4;32m{nova_cor}\033[m")
elif nova_cor == "AMARELO":
    print (f"\033[1;4;33m{nova_cor}\033[m")
elif nova_cor == "ROXO":
    print (f"\033[1;4;35m{nova_cor}\033[m")
elif nova_cor == "CINZA":
    print (f"\033[1;4;30m{nova_cor}\033[m")
elif nova_cor == "AZUL":
    print (f"\033[1;4;34m{nova_cor}\033[m")
elif nova_cor == "AZUL CLARO":
    print (f"\033[1;4;36m{nova_cor}\033[m")
else:
    print ("Não encontrado. Tente novamente!")
    print (linha)
print (linha)
n1 = int(input("Digite um número: "))
print (linha)
n2 = int(input("Digite outro número: "))
print (linha)
n3 = n1 + n2
print (linha)
print ("Os a soma é {}{}{} + {}{}{} = {}{}{}".format("\033[1;4;35m", n1, "\033[m","\033[1;4;32m", n2, "\033[m","\033[1;4;33m", n3, "\033[m" ))
print (linha)

nome = str(input("Digite seu nome: "))
cores = {"limpa":"\033[m",
         "cinza":"\033[30m",
         "pretoebranco": "\033[1;7m"}
print (linha)
print ("Olá! Muito prazer em te conhecer {}{}{}!".format(cores["pretoebranco"], nome, cores["limpa"]))
print (linha)
