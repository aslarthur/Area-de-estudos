#Crie o programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cidade = str(input("Digite o nome da sua cidade: ")).strip().lower()
santos = cidade [0]

if cidade.startswith ("santo"):
    print ('Sua cidade começa com "Santo"!')
else:
    print ("Que legal!")