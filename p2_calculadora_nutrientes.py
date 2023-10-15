# Crear un diccionario para almacenar la información nutricional por cada 100 gramos de cada ingrediente
info_nutricional = {}

# Solicitar al usuario ingresar los ingredientes y su información nutricional
num_ingredientes = int(input("Ingrese la cantidad de ingredientes en la receta: "))

for i in range(num_ingredientes):
    ingrediente = input(f"Ingrese el nombre del ingrediente {i+1}: ")
    proteinas = float(input(f"Ingrese la cantidad de proteínas por cada 100 gramos de {ingrediente}: "))
    carbohidratos = float(input(f"Ingrese la cantidad de carbohidratos por cada 100 gramos de {ingrediente}: "))
    grasas = float(input(f"Ingrese la cantidad de grasas por cada 100 gramos de {ingrediente}: "))
    info_nutricional[ingrediente] = (proteinas, carbohidratos, grasas)

# Solicitar al usuario ingresar los ingredientes y sus cantidades en la receta
ingredientes_receta = {}
num_porciones = float(input("Ingrese el número de porciones en la receta: "))

for i in range(num_ingredientes):
    ingrediente = input(f"Ingrese el nombre del ingrediente {i+1} en la receta: ")
    cantidad = float(input(f"Ingrese la cantidad de {ingrediente} en la receta (en gramos): "))
    ingredientes_receta[ingrediente] = cantidad

# Calcular los nutrientes totales en la receta
total_proteinas = 0
total_carbohidratos = 0
total_grasas = 0

for ingrediente, cantidad in ingredientes_receta.items():
    proteinas_por_100g, carbohidratos_por_100g, grasas_por_100g = info_nutricional[ingrediente]
    total_proteinas += (proteinas_por_100g * cantidad / 100) * num_porciones
    total_carbohidratos += (carbohidratos_por_100g * cantidad / 100) * num_porciones
    total_grasas += (grasas_por_100g * cantidad / 100) * num_porciones

# Mostrar el resultado
print(f"Nutrientes totales en la receta para {num_porciones} porciones:")
print(f"Proteínas: {total_proteinas} gramos")
print(f"Carbohidratos: {total_carbohidratos} gramos")
print(f"Grasas: {total_grasas} gramos")
