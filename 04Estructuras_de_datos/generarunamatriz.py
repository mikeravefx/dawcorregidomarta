import random

# Generar la matriz de forma simplificada en una sola línea
def crea_matriz_aleatoria(num_filas: int, num_columnas: int) -> list[list[int]]:
    return [[random.randint(0, 100) for i in range(num_columnas)] for j in range(num_filas)]

# Ejemplo de uso para crear la matriz
matriz = crea_matriz_aleatoria(6, 7)  # Generar una matriz de 6 filas y 7 columnas

# Función para contar los números pares e impares y devolver listas
def contarpares_impares(matriz: list[list[int]]) -> tuple[int, int, list[int], list[int]]:
    pares = 0
    impares = 0
    lista_pares = []
    lista_impares = []

    # Recorremos la matriz para contar los pares e impares
    for fila in matriz:
        for num in fila:
            if num % 2 == 0:
                pares += 1
                lista_pares.append(num)
            else:
                impares += 1
                lista_impares.append(num)
    
    return (pares, impares, lista_pares, lista_impares)

# Llamada a la función para contar pares e impares
resultado = contarpares_impares(matriz)

# Desempaquetamos el resultado
pares, impares, lista_pares, lista_impares = resultado

# Función para separar los pares e impares en listas, corregida
def paresimpares(matriz: list[list[int]]) -> tuple[list[int], list[int]]:
    pares = []
    impares = []
    
    # Recorremos la matriz para separar los números pares e impares
    for fila in matriz:
        for valor in fila:
            if valor % 2 == 0:
                pares.append(valor)
            else:
                impares.append(valor)
    
    return pares, impares

# Llamamos a la función paresimpares
pares_lista, impares_lista = paresimpares(matriz)

# Imprimimos el resultado
print(f"Pares: {pares}, Impares: {impares}")
print(f"Lista de Pares: {lista_pares}")
print(f"Lista de Impares: {lista_impares}")
print(f"Lista de Pares (función paresimpares): {pares_lista}")
print(f"Lista de Impares (función paresimpares): {impares_lista}")




    