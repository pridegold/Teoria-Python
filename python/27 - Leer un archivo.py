

with open("C:\\Users\\damia\\Desktop\\texto.txt") as archivo:
    print(archivo.read())


#print(archivo.closed) arroja true o false si el archivo esta cerrado

# Ahora usemos devuelta Try si la ruta estuviera mal escrita como a continuacion

try:
    with open("C:\\Users\\damia\\Desktop\\texto.tx") as archivo: # falta la t en .txt
        print(archivo.read())
except FileNotFoundError:
    print("El archivo no fue encontrado")
