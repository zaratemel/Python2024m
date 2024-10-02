from personaje import Personaje
#nombre,altura,velocida,resistencia,fuerza

menu = """
       
    1. Crear personaje
    2. Jugar
    3. Salir

 """

print(menu)


CantidadDePersonaje = 0

nuevo_personaje = [ ]

#tengo un error al ejecutar el codigo

while True:
    
    OpcionElegida = int(input("elejir una opcion: "))

    if OpcionElegida == 1:

        nombre = (input("Ingrese el nombre de su personaje: "))
        altura = int(input("Ingrese la altura de su personaje en centimetros: "))
        velocidad = int(input("Ingrese la cantidad de velocidad que tiene su personaje: "))
        resisitencia = int(input("ingrese la cantidad de resistencia que tiene su personaje: "))
        fuerza = int(input("Ingrese la cantidad de fuerza que tiene su personaje"))

        NuevoPersonaje = Personaje(nombre, altura, velocidad, resisitencia, fuerza)
        nuevo_personaje.append(NuevoPersonaje)
       
    elif OpcionElegida == 2:

        if CantidadDePersonaje == 0:
            print("no hay personajes para poder jugar")

        else:
            print("iniciando la carrera con los siguientes persanajes")
            for Personaje in nuevo_personaje:
                print(f" {Personaje.nombre}")

    
    elif OpcionElegida == 3:
        break

    else:
        print("la opcion no es correcta, intentelo más tarde")

       