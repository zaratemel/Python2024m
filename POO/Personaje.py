class Personaje:

    estado = True 
    vida = 100

    def __init__(self, nombre, altura, velocidad, resistencia, fuerza):
        self.nombre = nombre
        self.altura = altura
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.fuerza = fuerza
        self.estado = True
        self.vida = 100

    def atacar(self, otro_personaje):
        if not self.estado:
            print(f"{self.nombre} no puede atacar porque está muerto.")
            return

        if not otro_personaje.estado:
            print(f"{otro_personaje.nombre} no puede ser atacado porque está muerto.")
            return

        # Cálculo del daño
        danio = self.fuerza - otro_personaje.resistencia
        if danio < 0:
            danio = 0  # Si la resistencia es mayor que la fuerza, no se causa daño

        print(f"{self.nombre} ataca a {otro_personaje.nombre} causando {danio} de daño.")
        otro_personaje.recibirDanio(danio)

    def recibirDanio(self, cantidad):
        if self.estado:
            self.vida -= cantidad
            print(f"{self.nombre} recibe {cantidad} de daño. Vida restante: {self.vida}.")

            if self.vida <= 0:
                self.estado = False
                print(f"{self.nombre} ha muerto.")
        else:
            print(f"{self.nombre} ya está muerto, no puede recibir más daño.")

    def mostrar_info(self):
        estado_str = "vivo" if self.estado else "muerto"
        print(f"Nombre: {self.nombre}, Vida: {self.vida}, Estado: {estado_str}, Velocidad: {self.velocidad}, Resistencia: {self.resistencia}, Fuerza: {self.fuerza}")