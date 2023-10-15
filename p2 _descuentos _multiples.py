# Pedir al usuario el precio y la categoría
precio = float(input("Ingrese el precio del producto: "))
categoria = input("Ingrese la categoría (A, B o C): ")

# Pedir al usuario el número de unidades compradas
unidades = int(input("Ingrese el número de unidades compradas: "))

# Definir los descuentos según la categoría
descuento = 0
if categoria == "A":
    descuento = 0.10
elif categoria == "B":
    descuento = 0.05
elif categoria == "C":
    descuento = 0.02
else:
    print("Categoría no válida")

# Calcular el precio total con descuento
precio_total = precio * unidades * (1 - descuento)

# Mostrar el resultado
print(f"El precio total con descuento es: ${precio_total:.2f}")
