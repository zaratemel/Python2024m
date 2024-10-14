
import sqlite3

class Estudiante:

    def __init__(self, Nombre, Edad, Año_id):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Año_id = Año_id


    def guardar(self):

        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()

        c.execute('INSERT INTO Estudiantes(Nombre, Edad, Año_id) VALUES (?, ?, ?)',
        (self.Nombre, self.Edad, self.Año_id))


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
