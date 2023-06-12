# Multiple heredacion

class Organismos:
    
    alive = True
    def __init__(self,tipo,color): # Aca importe el orden de las cosas <--- ya que va a ser el orden en el cual se printeen cuando llamemos a las funciones
        
        self.tipo = tipo
        self.color = color
        

class Animal(Organismos):
    def mamifero(self):
        print(f"Este {self.tipo} de color {self.color} es mamifero")

class Caballo(Animal):
    def saltar(self):
        print(f"Este {self.tipo} de color {self.color} esta saltando")

caballo_1 = Caballo("Caballo", "Negro") #Con los () evitamos el error de que falte un argumento para self
print(caballo_1.alive)
caballo_1.saltar()