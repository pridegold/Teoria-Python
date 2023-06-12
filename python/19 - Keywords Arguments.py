

# Los keywords arguments nos permiten identificar un valor para pasarlo a la funcion, sin importar el orden



def hola(primero, segundo, tercero):
    print(f"Hola {primero} {segundo} {tercero}")


# En este caso sin Keywords, importaria el orden, ya que si cambio de lugar los valores, se veria distinto
hola("Damian","Ariel","Lopez")
hola("Ariel","Damian","Lopez")



# Pero si uso los Keywords no importa el orden en como los coloque a la hora de llamar a la funcion
hola(tercero="Lopez", primero="Damian", segundo="Ariel")  