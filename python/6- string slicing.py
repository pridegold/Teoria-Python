# El slicing nos permite crear strings sacando caracteres de las variables que tengamos, mediante index[] o slice()



#INDEX -> [start:stop:step] el INICIO INCLUYE, pero el STOP EXCLUYE, entonces siempre tenemos que agregar un espacio mas para tener lo que queremos del lado del stop, ejemplo

name = "Damian Lopez"

first_name1 = name[0:5] # esto da como resultado Damia, por eso deberiamos colocar 6 como stop
first_name = name[0:6] # tambien se puede dejar vacio el start, sin valor, ya que no alteraria el resultado osea name[:3]
print(first_name1)
print(first_name)

last_name = name[7:12] # se puede dejar vacio el final, ya que tampoco altera el resultado name[4:0]
print(last_name)

# Ahora el step, osea la 3er parte del slicing con index, indica cada cuantos caracteres queremos saltear en la variable

funky_name = name[0:8:2] # en este caso queremos los caracteres seleccionados cada 2 espacios.
print(funky_name)

reversed_name = name [::-1] # Para cambiar al orientacion del string, en este caso comienza de atras para adelante
print(reversed_name)


# SLICE -> Similiar al index, incluye el inicio, excluye el final. Se realiza con variables llamando a la funcion slice(). Ejemplos

website1 = "http://facebook.com"
website2 = "http://tycsports.com"

slice = slice(7,-4) #principio incluye final excluye

print(website1[slice])
print(website2[slice])





