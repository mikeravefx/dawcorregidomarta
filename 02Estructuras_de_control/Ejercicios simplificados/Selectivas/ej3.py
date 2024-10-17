# Escribe un programa en Python que:

# Pida al usuario un número entero y lo guarde en una variable

# Pida al usuario otro número entero y lo guarde en otra variable

# Determine cuál de los dos números es mayor y muestre un mensaje indicándolo

# Solicita al usuario el primer número entero
numero1 = int(input("Introduce el primer número entero: "))

# Solicita al usuario el segundo número entero
numero2 = int(input("Introduce el segundo número entero: "))

# Compara los dos números y muestra cuál es mayor
if numero1 > numero2:
    print(f"El número {numero1} es mayor que el número {numero2}.")
elif numero2 > numero1:
    print(f"El número {numero2} es mayor que el número {numero1}.")
else:
    print("Ambos números son iguales.")