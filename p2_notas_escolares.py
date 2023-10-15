# Inicializamos las variables
notas = []
total_estudiantes = int(input("Ingrese el número de estudiantes: "))

# Solicitamos las notas de los estudiantes
for i in range(total_estudiantes):
    nota = float(input(f"Ingrese la nota del estudiante {i + 1}: "))
    notas.append(nota)

# Calculamos el promedio, la nota más alta y la nota más baja
promedio = sum(notas) / total_estudiantes
nota_mas_alta = max(notas)
nota_mas_baja = min(notas)

# Contamos cuántos estudiantes aprobaron y reprobaron
aprobados = sum(nota >= 60 for nota in notas)
reprobados = total_estudiantes - aprobados

# Mostramos los resultados
print(f"Promedio de notas: {promedio:.2f}")
print(f"Nota más alta: {nota_mas_alta}")
print(f"Nota más baja: {nota_mas_baja}")
print(f"Estudiantes aprobados: {aprobados}")
print(f"Estudiantes reprobados: {reprobados}")
