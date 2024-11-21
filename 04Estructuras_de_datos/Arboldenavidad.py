altura = int(input("Introduce la altura del árbol de Navidad: "))
def arbol_navidad(altura: int) -> None:
# Estrella en la cima
    print(" " * (altura - 1) + "*")

# Ramas del árbol
for i in range(altura):
    espacios = " " * (altura - i - 1)
    ramas = "*" * (2 * i + 1)
    print(espacios + ramas)

# Tronco del árbol
for _ in range(2):
    print(" " * (altura - 1) + "||")

# Solicitar la altura del árbol al usuario

arbol_navidad(altura)

