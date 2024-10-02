class Personaje:

    estado = True 
    vida = 100

    def __init__(self,nombre,altura,velocida,resistencia,fuerza):

        self.nombre = nombre
        self.altura = altura
        self.velocida = velocida
        self.resistencia = resistencia
        self.fuerza = fuerza
        self.estado = Personaje.estado
        self.vida = Personaje.vida

    
    def atacar (self, NuevoPersonaje):
        if not self.estado:
            print(f"{self.nombre} no puede atacar porque esta muerto")
            return

        if not otro_personaje.estado:
            print(f"{otro_personaje.nombre} no puede atacar porque esta muerto")
            return
        
        danio = self.fuerza - otro_personaje.resistencia

        if danio < 0:
            danio = 0 

        print(f"{self.nombre} ataca a {NuevoPersonaje.nombre} causando {danio} de daño")
        NuevoPersonaje.recibirDanio(danio)
    
    def recibirDanio (self, cantidad):
  
        if self.estado:
            self.vida -= cantidad 
            print(f"{self.nombre} recibe {cantidad} de daño. Vida restante: {self.vida}.")

            if self.vida <= 0:
                self.estado = False
                print(f"{self.nombre} ha muerto.")

        else:
            print(f"{self.nombre} no puede recibir daño porque ya esta muerto")
            
def mostrar_info(self):
        estado_str = "vivo" if self.estado else "muerto"
        print(f"Nombre: {self.nombre}, Vida: {self.vida}, Estado: {estado_str}, Velocidad: {self.velocidad}, Resistencia: {self.resistencia}, Fuerza: {self.fuerza}")
    
