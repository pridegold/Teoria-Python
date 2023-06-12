# Nos permite definir una clase que heredan todos los metodos y propiedades de otra clase-
# Pensando que Animal seria el padre, y los tipos de animales los hijos, como para poder entenderlo de una manera mas directa

class Animal:

    alive = True

    def __init__(self, raza):
        self.raza = raza
        
    def comer(self):
        print(f"Este {self.raza} esta comiendo")

    def dormir(self):
        print(f"Este {self.raza} esta durmiendo")


class Perro(Animal):
    def correr(self):
        print(f"Este {self.raza} esta corriendo")

class Gato(Animal):
    def caer(self):
        print(f"Este {self.raza} esta cayendose")

class Conejo(Animal):
    def saltar(self):
        print(f"Este {self.raza} esta saltando")

perro_1 = Perro("GranDanes")
gato_1 = Gato("Siames")
conejo_1 = Conejo("Montes")


# Puedo llamar tanto a las funciones globales como a las locales, al haberles heredado a cada clase, la clase global animal.
perro_1.comer() 
gato_1.caer()
conejo_1.saltar()







