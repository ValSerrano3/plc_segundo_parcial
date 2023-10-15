import random

# Definición de personajes
personajes = {
    "Guerrero": {"vida": 10, "ataque": 8, "defensa": 6},
    "Mago": {"vida": 6, "ataque": 10, "defensa": 4},
    "Arquero": {"vida": 8, "ataque": 7, "defensa": 5},}

# Elige un personaje
print("Elige tu personaje:")
for personaje in personajes:
    print(personaje)

personaje_elegido = input("Ingresa el nombre del personaje: ")
if personaje_elegido in personajes:
    jugador = personajes[personaje_elegido]
    print(f"Has elegido al {personaje_elegido}. Vida: {jugador['vida']}, Ataque: {jugador['ataque']}, Defensa: {jugador['defensa']}")
else:
    print("Personaje no válido. Elige un personaje existente.")
    exit()
# Función para lanzar un dado
def lanzar_dado():
    return random.randint(1, 20)

# Simulación de un desafío
print("Te enfrentas a un dragón. Debes superar un desafío.")
resultado_del_dado = lanzar_dado()

if resultado_del_dado >= 10:  # Puedes ajustar esta condición según tus reglas
    print(f"Has tenido éxito al obtener {resultado_del_dado} en el dado.")
    print("¡Derrotaste al dragón!")
else:
    print(f"Has fallado al obtener {resultado_del_dado} en el dado.")
    print("El dragón te ha derrotado.")
