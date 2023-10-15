# Solicita al usuario ingresar la distancia en millas y el rendimiento en millas por galón
distancia_millas = float(input("Ingrese la distancia en millas: "))
rendimiento_mpg = float(input("Ingrese el rendimiento en millas por galón: "))

# Pregunta al usuario el precio actual de la gasolina por galón y cuántos días planea viajar
precio_gasolina = float(input("Ingrese el precio actual de la gasolina por galón: "))
dias_viaje = int(input("Ingrese cuántos días planea viajar: "))

# Calcula la cantidad de galones necesarios para el viaje
galones_necesarios = distancia_millas / rendimiento_mpg

# Inicializa el costo total del viaje
costo_total = 0.0

# Realiza un bucle para calcular el costo total considerando los precios cambiantes de la gasolina
for _ in range(dias_viaje):
    precio_gasolina_dia = float(input("Ingrese el precio de la gasolina por galón para este día: "))
    costo_total += galones_necesarios * precio_gasolina_dia

# Muestra el costo total del viaje
print(f"El costo total del viaje es de ${costo_total:.2f}")
