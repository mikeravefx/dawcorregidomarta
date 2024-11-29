import random
from colorama import Fore, init

# Inicializamos colorama
init(autoreset=True)

def imprimir_arbol():
    # Definimos el tamaño del árbol
    altura = 7
    
    # Colores para las luces titilantes
    colores_luces = [Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]
    
    # Imprimir las ramas del árbol con bambalinas rojas y luces titilantes
    for i in range(altura):
        # Calcular el número de espacios antes de los asteriscos
        espacios = ' ' * (altura - i - 1)
        # Crear la fila de estrellas
        fila = '*' * (2 * i + 1)
        
        # Crear la fila con bambalinas rojas (representadas por 'o') en posiciones aleatorias
        fila_con_bambalinas_y_luces = ''
        for j in range(len(fila)):
            if j % 2 == 0:  # Colocar bambalinas rojas en posiciones pares
                fila_con_bambalinas_y_luces += Fore.RED + 'o'
            else:
                # Agregar luces titilantes en algunas posiciones
                if random.random() < 0.2:  # 20% de probabilidades de agregar una luz titilante
                    color_luz = random.choice(colores_luces)
                    fila_con_bambalinas_y_luces += color_luz + '*'
                else:
                    fila_con_bambalinas_y_luces += fila[j]
        
        # Imprimir la fila con los espacios y las bambalinas + luces titilantes
        print(espacios + fila_con_bambalinas_y_luces)
    
    # Imprimir el tronco del árbol
    for i in range(2):
        print(' ' * (altura - 1) + '| |')

# Llamamos a la función para imprimir el árbol de Navidad
imprimir_arbol()
