# Escribe un programa qen Python que:

# Pida al usuario un número entero y lo guarde en una variable

# Muestre un mensaje indicando si el número es par o impar

# Solicita al usuario un número entero
numero = int(input("Introduce un número entero: "))

# Verifica si el número es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")