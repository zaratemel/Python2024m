
import sqlite3

class Profesor:

    def __init__ (self, Nombre_profesor, Materia, Id):
        self.Nombre_profesor = Nombre_profesor
        self.Materia = Materia
        self.Id = Id

    
    def guardar(self):

        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()

        c.execute('INSERT INTO Profesor(Nombre_profesor, Materia, Id) VALUES (?, ?, ?)',
        (self.Nombre_profesor, self.Materia, self.Id))


        conn.commit()
        conn.close()

    @staticmethod
    def obtener_Profesor():

        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()

        c.execute('SELECT * FROM Profesor')


        Profesor = c.fetchall()
        conn.close()

        return Profesor
