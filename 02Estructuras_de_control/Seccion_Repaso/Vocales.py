frase = input("Escribe tu frase: ")
ten_vogais = False
VOGAIS = "AEIOUÁÉÍÓÚÜaeiouáéíóúü"

for letra in frase:
    if letra in VOGAIS:
        ten_vogais = True
        break #Cando atopo unha vogal, xa non sigo buscando

if ten_vogais: # if ten_vogais == True:
    print("Ten vogais")
else:
    print("Non ten vogais")