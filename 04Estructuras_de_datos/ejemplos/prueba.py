tabla_multiplicar = []

for f in range(0,11):
    fila = []
    for c in range(0,11):
        fila.append(f * c)
    tabla_multiplicar.append(fila)

print(tabla_multiplicar)

for fila in tabla_multiplicar:
    print(fila)

for fila in tabla_multiplicar:
    for elemento in fila:
        print(elemento, end="\t")
    print()