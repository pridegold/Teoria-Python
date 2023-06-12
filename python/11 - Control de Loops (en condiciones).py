# Se pueden controlar, finalizar o pasar loops mediante:

# break = Se usa para terminar el loop completo

# continue = Salta a la siguiente iteracion del loop

# pass = No hace nada.


while True:

    nombre = input("Pone tu nombre ") 
    if nombre != "": # Para indicar que algo sea distinto a otra cosa se escribe !=, entonces el programa se va a repetir hasta que nombre sea distinto a nada. Osea, que tenga valor.
        break #Finaliza


telefono = "11-3456-4021"

for x in telefono:
    if x == "-": # De esta forma podemos excluir los - en la variable
        continue #Se continua el codigo
    print(x, end="") #Colocamos end="" por que si no, se printearia como un rango. Prueben al sacarlo y fijense.



for i in range (1,21):
    if i == 13: #Excluimos el numero 13 del conteo.
        pass # PlaceHolder, no hace nada.
    else:
        print(i)


