# Los return, retornan los valores/objetos al llamado. Estos valores y objetos son conocidos como el valor de lo que devuelve la funcion.


def multiplicacion (numero1, numero2):
    resultado = numero1 * numero2
    return resultado

(multiplicacion(6, 5)) # Aca el codigo estaria correcto, pero falta printearlo.
print(multiplicacion(6, 5))

# Podemos asignar la funcion a una variable
x = multiplicacion(3, 3)
print(x)


# Tambien hacerlo con user inputs.
z = int(input("Inserte el Numero 1 "))
y = int(input("Inserte el Numero 2 "))

print(multiplicacion(z, y))