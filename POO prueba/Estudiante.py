
import sqlite3

class Estudiante:

    estado = True

    def __init__(self, legajo_id, dni, nombre, apellido, edad, fecha_nacimiento, curso, email):
        self.legajo_id = legajo_id
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.curso = curso
        self.email = email


    def guardar(self):

        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()

        c.execute('INSERT INTO Estudiantes(nombre, apellido, edad, fecha_nacimiento, curso, email) VALUES (?, ?, ?)',
        (self.nombre, self.apellido, self.edad, self.fecha_nacimiento, self.curso, self.email))


        conn.commit()
        conn.close()

    @staticmethod
    def obtener_estudiante():

        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()

        c.execute('SELECT * FROM Estudiantes')


        Estudiantes = c.fetchall()
        conn.close()

        return Estudiantes

