# Funciones son bloques de codigo que son ejecutadas solo cuando son llamadas.

def f(x):
    print(5+x)

f(5) # Llamamos a la funcion y la argumentamos.
def hola(nombre):
    print(f"Hola {nombre},", end= " ")
    print("Que tengas buen dia")

hola("Damian") # Llamamos a la funcion y la argumentamos.


def nombre(nombre, apellido, edad): # En este caso la funcion puede recibir 3 argumentos.
    print(f"Hola {nombre} {apellido}, tenes {edad} años")


nombre("Damian","Lopez", 25) # Llamamos a la funcion y argumentamos.

