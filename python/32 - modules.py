import mensajes #importamos el modulo mensajes que creamos en el proyecto, el mismo contiene el codigo que utilizaremos
# modulos Contienen codigo de ptyhon, funciones, clases etc

mensajes.hola() # colocamos el nombre del modulo y llamamos el codigo que querramos, en este caso las funciones
mensajes.adios()


from mensajes import hola, adios # Podemos importar directamente las funciones de esta forma
hola() # Y ahora como importamos las funciones, podemos llamarlas de esta forma
adios()