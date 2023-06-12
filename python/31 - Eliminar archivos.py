import os
import shutil

ruta = "python\\prueba.txt" #Creen un archivo .txt dentro del proyecto donde esten trabajando, click derecho y copien la ruta (relative path)

#os.remove(ruta) .remove(variable) esto borraria el archivo

# Ahora volvamos con try si el archivo no se encuentra
try:
    os.remove(ruta)
except FileNotFoundError:
    print("Archivo no encontrado")

else:
    print(f"{ruta} a sido borrada")


ruta1 = "python\\carpeta_vacia" # Creen una carpeta vacia donde tengan el proyecto y copiamos devuelta el relative path


try:
    os.rmdir(ruta1) #.rmdir sirve para borrar la carpeta, pero si esta tuviera archivos dentro, nos daria un error tipo OSError ---> No permitido

except FileNotFoundError:
    print("Archivo no encontrado")

else:
    print(f"{ruta1} ha sido borrada")


ruta2 = "python\\carpeta"

try:
    #os.rmdir(ruta2)   # Como la carpeta en cuestion tiene archivos dentro, debemos importar el modulo shutil ---> import shutil (lo estarian viendo la linea 2 de este codigo)
    shutil.rmtree(ruta2) # Considerado un comando peligroso ya que pueda borrar todo lo que una carpeta contenga.
except FileNotFoundError:
    print("Archivo no encontrado")

else:
    print(f"{ruta2} ha sido borrada")

