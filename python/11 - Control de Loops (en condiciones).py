# Se pueden controlar, finalizar o pasar loops mediante:

# break = Se usa para terminar el loop completo

# continue = Salta a la siguiente iteracion del loop

# pass = No hace nada.


while True:

    nombre = input("Pone tu nombre ")
    if nombre != "":
        break


telefono = "11-3456-4021"

for x in telefono:
    if x == "-":
        continue
    print(x, end="")



for i in range (1,21):
    if i == 13:
        pass
    else:
        print(i)


