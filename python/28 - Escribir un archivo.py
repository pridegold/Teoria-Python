
oracion = "Hola\nEsto es un poco de texto\nSaludos" # Aca colocamos lo que queres cambiar en el archivo

with open("C:\\Users\\damia\\Desktop\\texto.txt", "w") as archivo: #Se utiliza ,"w" = write (escribir) para poder realizarle la modificaciones de escritura al archivo
    archivo.write(oracion)

# Al ejecutarlo se realiza la modificacion y podemos visualizarlo en el archivo