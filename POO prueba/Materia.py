
import sqlite3

class Materia:

    def __init__ (self, Nombre_materia, Id, Nombre_profesor):
        self.Nombre_materia = Nombre_materia
        self.Id = Id 
        self.Nombre_profesor = Nombre_profesor


    def guardar(self):

        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()

        c.execute('INSERT INTO Materias(Nombre_materia,Id,Nombre_profesor) VALUES (?, ?, ?)',
        (self.Nombre_materia, self.Id, self.Nombre_profesor))


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
