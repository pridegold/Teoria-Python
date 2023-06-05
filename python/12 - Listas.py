# Las listas se utilizan para almacenar multiples items en una sola variable

#Para formar la lista, los valores de la variable deben estar entre []
comida = ["pizza", "hamburgesa", "pancho"]



# print(comida[0]) #Llamamos a la variable y la posicion que queremos llamar. Como en slicing, se arranca contando desde 0
# En el caso 0 printearia pizza, lo bueno de las listas, en que pueden actualizarse en cualquier momento


comida[0] = "sushi" # Aca indicamos que el index 0 sea sushi, entonces pizza deja de existir.



comida.append("helado") # .append sirve para agregar algo a las listas
comida.remove("pancho") # .remove para borrar
comida.pop() # .pop remueve el ultimo elemento de la lista
comida.insert(0, "Pescado") # .insert, nos permite agregar a la fila un valor en una determinada posicion, en este caso 0, osea el primer valor de la lista.
comida.sort() # Ordena la lista alfabeticamente
# comida.clear() # Clear elimina todos los valores de la lista

for x in comida:
    print(x)


