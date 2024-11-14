
import sqlite3

class Calificacion:

    def __init__(self, Estudiante_id, Materia_id, Calificacion):

        self.Estudiante_id = Estudiante_id
        self.Materia_id = Materia_id
        self.Calificacion = Calificacion


    def guardar(self):

        conn = sqlite3.connect('Escolar.db')
        c = conn.cursor()

        c.execute('INSERT INTO Calificacion(Estudiante_id, Materia_id, Calificacion) VALUES (?, ?, ?)',
        (self.Estudiante_id, self.Materia_id, self.Calificacion))


        conn.commit()
        conn.close()

    @staticmethod
    def obtener_Calificacion():

        conn = sqlite3.connect('Escolar.db')
        c = conn.cursor()

        c.execute('SELECT * FROM Calificacion')


        Calificacion = c.fetchall()
        conn.close()

        return Calificacion

