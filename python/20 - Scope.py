# scope Es una region en la cual la variable es reconocida, la variable esta disponible solo dentro de la region donde esta creada
# Pueden ser locales y globales

apellido = "Lopez" # Global Scope --> Variable que tiene un acceso de manera global en el codigo

def display_name():
  nombre = "Damian"  # Esta variable es un tipo de scope local, ya que solo esta disponible dentro de la funcion.
  print(nombre)


display_name()
print(apellido) # Si no tuviera la variable GLOBAL fuera de la funcion, este print daria error, ya que no estaria definida la variable