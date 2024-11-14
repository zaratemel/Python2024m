
import sqlite3

class Profesor:

    estado = True

    def __init__ (self, dni_id, nombre, apellido, curso, email):
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.email = email

    
    def guardar(self):

        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()

        c.execute('INSERT INTO Profesor(nombre, apellido, curso, email) VALUES (?, ?, ?)',
        (self.nombre, self.apellido, self.curso, self.email))


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
