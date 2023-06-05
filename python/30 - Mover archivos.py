import os

origen = "python\\prueba.txt" #Creen un archivo .txt dentro del proyecto donde esten trabajando, click derecho y copien la ruta
destino = "C:\\Users\\damia\\Desktop\\archivoCopiado.txt"

try:
    if os.path.exists(destino):
        print("Ya hay un archivo ahi")
    else:
        os.replace(origen, destino)
        print(f"{destino} fue movido")

except FileNotFoundError:
    print(f"{origen} no fue encontrado")

