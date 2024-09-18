from personaje import Personaje
#nombre,altura,velocida,resistencia,fuerza

menu = """
       
    1. Crear personaje
    2. Jugar
    3. Salir

 """

print = (menu)

OpcionElegida = int(input("elejir una opcion"))

CantidadDePersonaje = 0

p + CantidadDePersonaje = [ ]

#tengo un error al ejecutar el codigo

while True:

    if OpcionElegida == 1:

        Nombre = input("Ingrese el nombre de su personaje: ")
        Altura = int(input("Ingrese la altura de su personaje en centimetros: ")
        Velocidad = int(input("Ingrese la cantidad de velocidad que tiene su personaje: "))
        Resisitencia = int(input("ingrese la cantidad de resistencia que tiene su personaje: "))
        Fuerza = int(input("Ingrese la cantidad de fuerza que tiene su personaje"))

        nuevo_personaje = Personaje(Nombre, altura, Velocidad, Resisitencia, Fuerza)
        per
       
    elif OpcionElegida == 2:

        if CantidadDePersonaje == 0:
            print("no hay personajes para poder jugar")

        else:
            print("iniciando la carrera con los siguientes persanajes")
            for Personaje in personajes:
                print(f" { }")

    
    elif OpcionElegida == 3:
        break

    else:
        print("la opcion no es correcta, intentelo más tarde")

       