# Solicitar la edad actual del usuario
edad_actual = int(input("Ingrese su edad actual: "))

# Solicitar la edad de jubilación deseada
edad_jubilacion = int(input("Ingrese la edad a la que planea jubilarse: "))

# Calcular el número de años hasta la jubilación
años_hasta_jubilacion = edad_jubilacion - edad_actual

# Solicitar la cantidad deseada para la jubilación
cantidad_deseada = float(input("Ingrese la cantidad deseada para la jubilación: "))

# Solicitar la tasa de interés anual esperada en forma decimal
tasa_interes_anual = float(input("Ingrese la tasa de interés anual esperada (por ejemplo, 0.06 para 6%): "))

# Calcular la tasa de interés mensual
tasa_interes_mensual = tasa_interes_anual / 12

# Calcular el número de pagos mensuales en la jubilación (años de jubilación multiplicados por 12)
n = años_hasta_jubilacion * 12

# Calcular el pago mensual necesario utilizando la fórmula PMT
pago_mensual_necesario = cantidad_deseada / ((1 + tasa_interes_mensual) ** n - 1) * tasa_interes_mensual

# Mostrar el resultado
print(f"Debería ahorrar ${pago_mensual_necesario:.2f} mensualmente para alcanzar su objetivo de jubilación.")
