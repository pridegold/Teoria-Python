import random   

z = random.randint(1, 3) # .randint devuelte numeros int aleatorios


juego = ["piedra", "papel", "tijera"]
x = random.choice(juego) # Creamos una variable aleatoria teniendo en cuenta la lista juego
cartas = [1,2,3,4,5,6,7,"J","Q","K"]
random.shuffle(cartas) # Mezclamos el orden los valores de la variable cartas

print(cartas)
print(x)
print(z)