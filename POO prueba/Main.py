from Estudiante import Estudiante
from Materia import Materia
from Profesor import Profesor
from Calificacion import Calificacion

def menu():
    while True:

        print('''
        Menu
        1. Estudiantes
        2. Materias
        3. Profesores
        4. Calificaciones
        5. Salir
        ''')

        opcion = int(input('elija una opcion: '))

        if opcion == 1:
            gestionar_estudiante()

        elif opcion == 2:
            gestionar_materias()
        
        elif opcion == 3:
            gestionar_profesores()

        elif opcion == 4:
            gestionar_calificaciones()

        elif opcion == 5:
            print('saliendo del programa')
            break

        else: 
            print('opcion invalida, intentelo de nuevo')
            

def gestionar_estudiante():

    while True:

        print('''
        Elija una opcion
        1. Agregar estudiante
        2. buscar estudiante
        3. volver al menu principal

        ''')

        opcion = int(input('Cual opcion desea: '))

        if opcion == 1:
            print('Porfavor complete lo siguiente')
            dni = int(input('ingrese el dni del nuevo estudiante: '))
            nombre = input('ingrese el nombre del estudiante: ')
            apellido = input('ingrese el apellido del estudiante: ')
            edad = int(input('ingrese la edad del estudiante: '))
            fecha_nacimiento = input('ingrese la fecha de nacimiento del estudiante: ')
            curso = input('ingrese el curso del estudiante: ')
            email = input('ingrese el email del estudiante: ')

            estudiante = Estudiante(None, dni, nombre, apellido, edad, fecha_nacimiento, curso, email)

            estudiante.guardar()
            print('Estudiante agregado con exito')


def gestionar_materias():
    print('aa')
    

def gestionar_profesores():
    print('ff')

def gestionar_calificaciones():
    print('gg')

#luego agrego lo que falta