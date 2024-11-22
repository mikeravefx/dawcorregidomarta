notas = [[5, 5, 4], [4, 5, 6], [8, 9, 10]]
modulos = ['a', 'b', 'c']
alumnos = ['Miguel', 'Juan', 'Gabriel']
resultado = []

# Calculamos el promedio por cada alumno
for notas_alumnos in range(len(notas)):
    suma = 0
    for columna in range(len(notas[notas_alumnos])):
        suma += notas[notas_alumnos][columna]
    media = suma / len(notas[notas_alumnos])
    resultado.append(media)

# Imprimimos la tabla con las notas de cada alumno por módulo
print("Notas de los alumnos:")
for i in range(len(alumnos)):
    print(f'Alumno: {alumnos[i]}')
    for j in range(len(modulos)):
        print(f'\tMódulo {modulos[j]}: {notas[i][j]}')
    print(f'\tPromedio: {resultado[i]:.2f}')
    print('-' * 30)

# Calculamos el promedio por módulo y lo imprimimos
print("Promedio por módulo:")
for j in range(len(modulos)):
    suma_modulo = 0
    for i in range(len(notas)):
        suma_modulo += notas[i][j]
    promedio_modulo = suma_modulo / len(notas)
    print(f'Módulo {modulos[j]}: Promedio {round(promedio_modulo,2)}')