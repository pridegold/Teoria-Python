# str.format() Un metodo opcional que le da al usuario mas control cuando ejecuta outputs

animal = "Vaca"
item = "Luna"
# Debemos printear utilizando {} donde iran los valores de los strings, finalizando con .format(), se puede realizar de las siguientes formas
print("La {} salto sobre la {}".format(animal, item)) # Pasando el print con .format() y colocando las variables o valores directamente
print("La {1} salto sobre la {0}".format(animal, item)) # Se puede seleccionar mediante orden por index.
print("El {vivo} salto sobre el {sistema}".format(vivo="Canguro", sistema="Sol")) # Mediante variable directamente para cambiarle el contenido

numero = 3.14159
numero1 = 1000
print("El numero pi es {:.2f}".format(numero)) #.f es para .floating number, entonces solo voy a tomar los 2 decimales de dicho numero en cuestion en este caso
print("El numero pi es {:,}".format(numero1)) # Para agregarle una , o . al numero
