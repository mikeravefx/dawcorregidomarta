# Escribe un programa en Python que:

# Pida al usuario un número entero y lo guarde en una variable

# Indique si el número es par, impar o cero

# Solicita al usuario un número entero
numero = int(input("Introduce un número entero: "))

# Verifica si el número es cero, par o impar
if numero == 0:
    print("El número es cero.")
elif numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")