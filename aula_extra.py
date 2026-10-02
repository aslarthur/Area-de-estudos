def linha():
    print ("-=" * 30)
while True:
    print ()
    linha()
    print ("Bem vindo(a)!")
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
    print (f"\033[30mSimples\033[m")
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
        print (f"\033[1;4;37m{cor}\033[m")
        código = "37"
    elif cor == "SIMPLES":
        print (f"\033[1;4;30mNENHUM\033[m")
        código = "30"
    else:
        linha()
        print (f"\033[1;4;31mCor não encontrada! Tente novamente.\033[m")
        continue
    break
linha()
print ("FUNDOS:")
while True:
    linha()
    print (f"\033[1;4;37;47mBranco\033[m")
    linha()
    print (f"\033[1;4;31;41mVermelho\033[m")
    linha()
    print (f"\033[1;4;32;42mVerde\033[m")
    linha()
    print (f"\033[1;4;33;43mAmarelo\033[m")
    linha()
    print (f"\033[1;4;34;44mAzul\033[m")
    linha()
    print (f"\033[1;4;35;45mRoxo\033[m")
    linha()
    print (f"\033[1;4;36;46mAzul claro\033[m")
    linha()
    print (f"\033[1;4;30;40mCinza\033[m")
    linha()
    print (f"\033[30;4mNenhum\033[m")
    linha()
    novo_fundo = str(input("Digite o fundo que você ira querer: "))
    linha()
    fundo = novo_fundo.upper().strip()
    if fundo == "BRANCO":
        print (f"\033[1;4;{código};47mFUNDO: BRANCO, TEXTO: {cor}\033[m")
    elif fundo == "VERMELHO":
        print (f"\033[1;4;{código};41mFUNDO: VERMELHO, TEXTO: {cor}\033[m")
    elif fundo == "VERDE":
        print (f"\033[1;4;{código};42mFUNDO: VERDE, TEXTO: {cor}\033[m")
    elif fundo == "AMARELO":
        print (f"\033[1;4;{código};43mFUNDO: AMARELO, TEXTO: {cor}\033[m")
    elif fundo == "AZUL":
        print (f"\033[1;4;{código};44mFUNDO: AZUL, TEXTO: {cor}\033[m")
    elif fundo == "ROXO":
        print (f"\033[1;4;{código};45mFUNDO: ROXO, TEXTO: {cor}\033[m")
    elif fundo == "AZUL CLARO":
        print (f"\033[1;4;{código};46mFUNDO: AZUL CLARO, TEXTO: {cor}\033[m")
    elif fundo == "CINZA":
        print (f"\033[1;4;{código};40mFUNDO: CINZA, TEXTO: {cor}\033[m")
    elif fundo == "NENHUM":
        print (f"\033[1;4;{código}mFUNDO: NENHUM, TEXTO: {cor}\033[m")
    else:
        linha()
        print (f"\033[1;4;31mNão encontrado! Tente novamente.\033[m")
        continue
    break
linha()