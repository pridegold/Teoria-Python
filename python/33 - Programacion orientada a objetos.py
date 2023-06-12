from classes import Car


auto_1 = Car("Chevrolet","Corvette", 2023,"Dorado") #Valores para el objeto construido
auto_2 = Car("Ferrari","Street", 2021,"Rojo")
moto_1 = Car("Ducati","Street", 2023,"Roja")

#Car.ruedas = 2, esto cambiara todo el valor de ruedas a 2, ya que es global
moto_1.ruedas = 2 #Class variable que puede ser cambiada
auto_1.conducir() #Llamo a las funciones junto con el objeto deseador
auto_1.Color()
print(auto_1.ruedas)
print(moto_1.ruedas)
