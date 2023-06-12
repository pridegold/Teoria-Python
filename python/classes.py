class Car:
    
    ruedas = 4 #class variable

    def __init__(self,marca,modelo,año,color):
         self.marca = marca
         self.modelo = modelo
         self.año = año
         self.color = color

    def conducir(self):
        print(f"Este {self.modelo} del año {self.año} se esta moviendo")

    def Color(self):
        print(f"Tiene un color {self.color} muy llamativo! ")


