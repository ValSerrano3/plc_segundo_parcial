# Función para convertir millas a kilómetros
def millas_a_kilometros(millas):
    return millas * 1.60934

# Función para convertir litros a galones
def litros_a_galones(litros):
    return litros * 0.264172

# Función para convertir grados Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Solicitar al usuario la cantidad y la unidad de origen
cantidad = float(input("Ingrese la cantidad a convertir: "))
unidad_origen = input("Ingrese la unidad de origen (millas, litros, o grados Fahrenheit): ")

# Solicitar al usuario la unidad de destino
unidad_destino = input("Ingrese la unidad de destino (kilómetros, galones, o grados Celsius): ")

# Realizar la conversión según la unidad de origen y destino
resultado = 0

if unidad_origen == "millas" and unidad_destino == "kilómetros":
    resultado = millas_a_kilometros(cantidad)
elif unidad_origen == "litros" and unidad_destino == "galones":
    resultado = litros_a_galones(cantidad)
elif unidad_origen == "grados Fahrenheit" and unidad_destino == "grados Celsius":
    resultado = fahrenheit_a_celsius(cantidad)
else:
    print("No se pudo realizar la conversión. Verifique las unidades ingresadas.")

# Mostrar el resultado
print(f"{cantidad} {unidad_origen} es igual a {resultado:.2f} {unidad_destino}.")
