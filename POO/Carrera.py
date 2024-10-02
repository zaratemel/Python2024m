from personaje import Personaje

menu = """
    1. Crear personaje
    2. Jugar
    3. Salir
"""

print(menu)

nuevo_personaje = []

while True:
    OpcionElegida = int(input("Elija una opción: "))

    if OpcionElegida == 1:
        nombre = input("Ingrese el nombre de su personaje: ")
        altura = int(input("Ingrese la altura de su personaje en centímetros: "))
        velocidad = int(input("Ingrese la cantidad de velocidad que tiene su personaje: "))
        resistencia = int(input("Ingrese la cantidad de resistencia que tiene su personaje: "))
        fuerza = int(input("Ingrese la cantidad de fuerza que tiene su personaje: "))

        # Crear nuevo personaje
        NuevoPersonaje = Personaje(nombre, altura, velocidad, resistencia, fuerza)
        nuevo_personaje.append(NuevoPersonaje)
        print(f"Personaje {nombre} creado exitosamente.\n")

    elif OpcionElegida == 2:
        if len(nuevo_personaje) == 0:
            print("No hay personajes para poder jugar.")
        else:
            print("Iniciando la carrera con los siguientes personajes:")
            
            # Mostrar los personajes antes de la carrera
            for personaje in nuevo_personaje:
                print(f"Personaje: {personaje.nombre}, Velocidad: {personaje.velocidad}")

            # Simulación simple de carrera: el personaje con más velocidad gana
            ganador = max(nuevo_personaje, key=lambda p: p.velocidad)
            print(f"\n¡El ganador de la carrera es {ganador.nombre} con una velocidad de {ganador.velocidad}!")

    elif OpcionElegida == 3:
        print("Saliendo del juego...")
        break

    else:
        print("La opción no es correcta, inténtelo de nuevo.\n")