frase = "Curso em Video Python Gustavo Guanabara"

print ("________________________________________________________")
print (f"quantos caracteres a frase {frase} tem: ", len (frase))
print ("________________________________________________________")

print (f"a frase {frase} tem", frase.count ("o"), "letra(s) o")
print ("________________________________________________________")

print (f"Da letra 0 até a letra 14, a frase {frase} tem ", frase.count ("o", 0, 14), "letra(s) o")
print ("________________________________________________________")

print ("A palavra deo começou na letra ", frase.find("deo"), "da frase")
print ("________________________________________________________")

print ("Existe a palavra Curso na frase? ","Curso" in frase)