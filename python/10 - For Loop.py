import time #importamos el tiempo, usualmente todas las importaciones se hacen en la primer linea de codigo

# A diferencia de los while loops, los for loops se ejecutan una cantidad limitada de veces


#for x in range(10): Esto me devolveria un rango de 1 a 9 ---> le agregamos +1 al print para que me devuelva el 10, recuerden que es excluyente en donde finaliza.
    #print(x+1)


#for i in range (50,100): Aca devolveria de 50 a 99, pero tambien le agregamos +1
    #print(i+1)

#for z in "Damian": aca nos devuelve nuestro nombre en rango
    #print(z)


import time
for segundos in range(0,10,): # Realizamos un programa que contee de final a principio. (inicio:fin:reverse) Para ello colocamos al final -1, para que sea en reversa
    print(segundos)
    time.sleep(1) # Hacemos que el conteo descanse 1 segundo entre cada dato que nos arroje

print("Feliz año nuevo!")


