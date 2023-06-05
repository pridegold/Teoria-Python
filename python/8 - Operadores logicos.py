# Operadores logicos (and, or, not)



temperatura = int(input("Cual es la temperatura afuera?: "))

if temperatura >= 0 and temperatura <= 30:  # And: Se deben cumplir las 2 condiciones que se plantea para que me devuelva un resultado
    print("La temperatura es linda hoy")
    print("Sali a caminar!")




elif temperatura < 0 or temperatura > 30:
    print("La temperatura es mala el dia de hoy") # Or: Se debe cumplir al menos 1 de las 2 condiciones para que me devuelta un resultado
    print("Quedate en casa")



numero = int(input("Ingresa un numero positivo "))

if numero < 0:
    print("Numero no valido, ingrese solo numeros positivos")
    numero = int(input("Ingresa un numero positivo "))
    

elif not(numero > 9):                         
    print("Tu numero tiene 1 cifra")  # Not: Devuelve un resultado opuesto a lo que se plantea, ya sea de Verdadero a Falso o biceversa.
# En este caso si pongo un numero menor a 9 me va a devolver un print, y si pongo algo mayor a 9 simplemente finaliza. 

