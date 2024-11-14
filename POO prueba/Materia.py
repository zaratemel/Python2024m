
import sqlite3

class Materia:

    def __init__ (self, id_materia, nombre, curso, describcion, horario):
        self.id_materia = id_materia
        self.nombre = nombre
        self.curso = curso
        self.describcion = describcion
        self.horario = horario


    def guardar(self):

        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()

        c.execute('INSERT INTO Materias(nombre, curso, describcion, horario) VALUES (?, ?, ?)',
        (self.nombre, self.curso, self.describcion, self.horario))


        conn.commit()
        conn.close()

    @staticmethod
    def obtener_Materias():

        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()

        c.execute('SELECT * FROM Materias')


        Materia = c.fetchall()
        conn.close()

        return Materia
