# Los diccionarios en Python nos permiten almacenar una serie de mapeos entre dos conjuntos de elementos, llamados keys and values (Claves y Valores).


Capitales = {"USA":"Washington DC",
             "Argentina":"Buenos Aires",
             "China":"Beijing",
             "Rusia":"Moscu"}



# Capitales.update({"USA":"Las vegas"}) <-- Esto actualizaria el valor de una key del diccionario, en este caso usa, pasaria de washington dc a Las vegas.

Capitales.pop("China") # Borrar china del diccionario

# Capitales.clear # Borraria todo mi set

print(Capitales.keys()) # Visualizar las claves
print(Capitales.values()) # Visualizar los valores
print(Capitales.items()) # Visualizar Claves y Valores.

print(Capitales["Rusia"]) # Devuelve el valor de la key Rusia, en este caso, moscu.
# print(Capitales["Alemania"]) Esto arrojaria error, por que alemania no esta en mi diccionario

# La forma correcta de utilizar los diccionario es utilizando .get, para obtener el valor de las key's

print(Capitales.get("Argentina"))
print(Capitales.get("Alemania")) # Aca en vez de error, arrojaria none. Y el programa podria continuar.

# Modifiquemos el diccionario
Capitales.update({"Alemania":"Berlin"})

# Ahora podemos utilizar for por ejemplo de la siguiente forma

for key,value in Capitales.items(): # Para la key,value en mi variable Capitales, llamos a los items() y printeo key,value, devolviendome todas las claves y valores del mismo.
    print(key,value)





