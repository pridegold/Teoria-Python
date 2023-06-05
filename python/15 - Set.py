# Set es una coleccion no ordenadas, no indexeada y sin valores duplicados.


cocina = {"tenedor", "cuchara", "cuchillo"}
elementos = {"bowl", "plato", "copa"}




cocina.add("Servilleta")
cocina.remove("tenedor")
# cocina.clear() <--- borra todo. Los comandos en los sets, son parecidos a las listas
cocina.update(elementos) # Agregamos al set de cocina, los elementos.


# for x in cocina: # Si ejecuto el codigo multiples veces seguidas, podemos ver como se va alterando el orden de los valores. Por eso un set es no ordenado.
    # print(x)


# Ahora... tambien podemos crear una variable la cual contenga los 2 sets!
cena = cocina.union(elementos) #Unimos mediante .union los 2 sets
for i in cena:
    print(i)

print(cocina.difference(elementos)) # Mediante .difference, el programa nos devolvera en forma de set, los valores que contiene un set, que le faltan al otro.
print(cocina.intersection(elementos))
print(cocina)



