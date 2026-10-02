def linha():
    print ("-=" * 30)
while True:
    def linha():
       print ("-=" * 30)
    print ()
    linha()
    print ("Bem vindo(a!")
    linha()
    print ("CORES DE TEXTO:")
    linha()
    print (f"\033[1;4;37mBranco\033[m")
    linha()
    print (f"\033[1;4;31mVermelho\033[m")
    linha()
    print (f"\033[1;4;32mVerde\033[m")
    linha()
    print (f"\033[1;4;33mAmarelo\033[m")
    linha()
    print (f"\033[1;4;34mAzul\033[m")
    linha()
    print (f"\033[1;4;35mRoxo\033[m")
    linha()
    print (f"\033[1;4;36mAzul claro\033[m")
    linha()
    print (f"\033[1;4;30mCinza\033[m")
    linha()

    nova_cor = str(input("Digite a cor que ira querer: "))
    linha()
    cor = nova_cor.upper().strip()
    if cor == "BRANCO":
        print (f"\033[1;4;30m{cor}\033[m")
        código = "30"
    elif cor == "VERMELHO":
        print (f"\033[1;4;31m{cor}\033[m")
        código = "31"
    elif cor == "VERDE":
        print (f"\033[1;4;32m{cor}\033[m")
        código = "32"
    elif cor == "AMARELO":
        print(f"\033[1;4;33m{cor}\033[m")
        código = "33"
    elif cor == "AZUL":
        print (f"\033[1;4;34m{cor}\033[m")
        código = "34"
    elif cor == "ROXO":
        print (f"\033[1;4;35m{cor}\033[m")
        código = "35"
    elif cor == "AZUL CLARO":
        print (f"\033[1;4;36m{cor}\033[m")
        código = "36"
    elif cor == "CINZA":
        print (f"\033[1;4;37{cor}\033[m")
        código = "37"
    else:
        linha()
        print ("Cor não encontrada! Tente novamente.")
        continue
    break
linha()
print ("FUNDOS:")
while True:
    linha()
    print (f"\033[1;37;47mBranco\033[m")
    linha()
    print (f"\033[1;31;41mVermelho\033[m")
    linha()
    print (f"\033[1;32;42mVerde\033[m")
    linha()
    print (f"\033[1;33;43mAmarelo\033[m")
    linha()
    print (f"\033[1;34;44mAzul\033[m")
    linha()
    print (f"\033[1;35;45mRoxo\033[m")
    linha()
    print (f"\033[1;36;46mAzul claro\033[m")
    linha()
    print (f"\033[1;30;40mCinza\033[m")
    linha()
    novo_fundo = str(input("Digite o fundo que você ira querer: "))
    fundo = novo_fundo.upper()
    if fundo == "BRANCO":
        print (f"\033[1;4;{código};47mFUNDO BRANCO E {cor}\033[m")
        break