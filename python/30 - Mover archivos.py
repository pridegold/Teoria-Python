import os

origen = "python\\prueba.txt" #Creen un archivo .txt dentro del proyecto donde esten trabajando, click derecho y copien la ruta
destino = "C:\\Users\\damia\\Desktop\\archivoCopiado.txt" # Donde queremos que sea movido y podemos cambiarle el nombre

try:
    if os.path.exists(destino): # Si el destino existe..
        print("Ya hay un archivo ahi")
    else: # Si no existe..
        os.replace(origen, destino) # Que sea reemplazado con el origen hacia destino
        print(f"{destino} fue movido")

except FileNotFoundError: #Exceptuamos el error
    print(f"{origen} no fue encontrado")

