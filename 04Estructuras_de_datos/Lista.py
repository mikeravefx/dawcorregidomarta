import random
filas = 6
columnas = 7

listota2 = [[random.randint(0, 9) for i in range(filas)] for j in range(columnas)] #para crear la matriz con número aleatorios

print(listota2)

lista_pares = [listota2[i][j] for i in range(len(listota2)) for j in range(len(listota2[i])) if listota2[i][j] % 2 == 0]
lista_impares = [listota2[i][j] for i in range(len(listota2)) for j in range(len(listota2[i])) if listota2[i][j] % 2 != 0]

# recorre la lista i j y verifica los numeros pares de lista

print("Lista Pares", lista_pares)
print()
print("Lista impares", lista_impares)
