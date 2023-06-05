# Convertir un tipo de data a otro

x = 1
y = 2.0
z = "3" 
print(y) # Aca lo vemos como un Float.
print(int(y))  # <---- Una de las maneras de convertir del tipo de data en este caso de Float a Int seria de la siguiente forma

print(x) # int
print(z*3) # Aca vemos como es un string, nos devuelve el mismo 3 veces.

z = int(z) # Lo convertimos a int de esta forma
print(z*3) # Ahora realiza la multiplicacion correctamente.

# Lo mismo podriamos hacer con Y

print(y*2) # Nos devuelte un resultado en data Float
y = int(y)  # Convertimos a int
print(y*2) # Resultado en int.