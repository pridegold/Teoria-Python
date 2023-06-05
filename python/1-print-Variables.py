#Teoria Python Damian Lopez Peduzzi

# Print para escribir

print("hola mundo")

# Variables y Data

## INTEGERS

edad = 25
jugadores = 2
cantidad = 5
print(edad)
print(f"Yo tengo {edad} años") # ---> un print normal seria print("Hola mundo") ---> Pero como queremos printear la variable debemos hacerlo con f, para permitir que esta se printee.
print(f"Yo tengo {jugadores} jugadores")
print(f"Yo tengo {cantidad} perros")


## FLOAT
# Variables que pueden contener decimales como por ejemplo 
numero = 20.5
print(numero)

#String

name = "Damian"
food = "Pizza"

print(F"mi nombre es {name} y mi comida favorita es la {food}")

# boolean son solo verdadero o falso

online = True
for_sale = False
running = False

if running:
    print ("The game is on") # ---> if/else/for/break se ve mas adelante. No se queden mucho con esto

else:
    print ("The game is off")

# Para ahorrar espacio podemos asignar las variables de manera multiple

x, y, z = 1, 2, 3

#print(x,y,z)

altura = 1.75

print(F"mi altura es {altura} cm")

