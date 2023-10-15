# Solicitar al usuario su peso en kg
peso = float(input("Ingrese su peso en kg: "))

# Solicitar la duración de la actividad en minutos
duracion = float(input("Ingrese la duración de la actividad en minutos: "))

# Solicitar el tipo de actividad
actividad = input("Ingrese el tipo de actividad (correr, nadar, andar en bicicleta, etc.): ")

# Definir un diccionario con valores aproximados de calorías quemadas por minuto para algunas actividades
calorias_por_minuto = {
    "correr": 9.8,
    "nadar": 7.0,
    "andar en bicicleta": 7.5,
    # Puedes agregar más actividades y sus respectivas tasas de calorías por minuto aquí
}

# Verificar si la actividad ingresada está en el diccionario
if actividad in calorias_por_minuto:
    tasa_calorias_por_minuto = calorias_por_minuto[actividad]
    # Calcular las calorías quemadas
    calorias_quemadas = duracion * tasa_calorias_por_minuto
    # Mostrar el resultado
    print(f"Usted quemó aproximadamente {calorias_quemadas:.2f} calorías durante la {actividad}.")
else:
    print("Actividad no encontrada en la base de datos. Intente con otra actividad o verifique la ortografía.")
