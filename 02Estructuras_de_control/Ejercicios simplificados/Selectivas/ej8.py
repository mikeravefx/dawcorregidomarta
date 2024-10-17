# Escribe un programa en Python que:

# Pida una nota en número y devuelva la calificación correspondiente

# Menor que 5: Suspenso

# Entre 5 y 6: Aprobado

# Entre 6 y 7: Bien

# Entre 7 y 9: Notable

# Mayor o igual que 9: Sobresaliente

# Solicita al usuario una nota
nota = float(input("Introduce una nota (0-10): "))

# Determina la calificación correspondiente
if nota < 5:
    calificacion = "Suspenso"
elif 5 <= nota < 6:
    calificacion = "Aprobado"
elif 6 <= nota < 7:
    calificacion = "Bien"
elif 7 <= nota < 9:
    calificacion = "Notable"
else:
    calificacion = "Sobresaliente"

# Muestra la calificación
print(f"La calificación correspondiente a la nota {nota} es: {calificacion}.")
