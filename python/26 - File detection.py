import os
# Creen un archivo de notas en el escritorio, con el nombre texto, y en propiades de ese archivo copien la ruta
# Si les aparece la direccion con solo una \, deben agregar otra mas como aparece a continuacion. Si no, no se podra hacer la deteccion.

ruta = "C:\\Users\\damia\\Desktop\\texto.txt" 
if os.path.exists(ruta): # Condicionamos si la ruta en cuestion existe primero
    print("La ubicacion existe")
    if os.path.isfile(ruta): # Si es un archivo
        print("Esto es un archivo")
    elif os.path.isdir(ruta): # Si es una carpeta
        print("Eso es una carpeta")

else: # Si no existe.
    print("La ubicacion no existe")



