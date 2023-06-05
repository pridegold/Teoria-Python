
# Las condiciones if se van a ejecutar mientras den como resultado True



edad = int(input("Cuantos años tenes?: "))


if edad >= 18:  # Condicionamos la variable edad, que si es mayor igual a 18, nos devuelva que somos mayores de edad
    print("Sos mayor de edad") # <- Siempre esten atentos a la indexacion del codigo, cuando apreten enter en la parte del if se les genera una sangria, para respetar el bloque de codigo


elif edad < 0: # La  condicion elif es para que el codigo siga buscando resultados si la condicion if no se cumple en un principio. Pueden haber multiples condiciones elif.
    print("Todavia no naciste")

elif edad >= 100:
    print("Vivis hace un centenar!") # 100 años lo cual seria correcto para esta condicion, me va a devolver unicamente el primer resultado, "Sos mayor de edad", por que es la primer condicion que se cumple.


else:  # Si las condiciones if y elif no dieron resultado, podemos dejarlo vacio y que termine el codigo, o tener una condicion else para tener un resultado cuando no se cumplan las instrucciones
    print("Sos menor de edad") # <--- Aca sucede lo mismo con respecto a la indexacion del codigo







numero = int(input("Ingresa un numero: "))

#if numero % 2 == 0:
#print(f"{numero} es par")   # <---- Ejemplo de como una indexacion puede arruinarles el codigo 

#if numero % 2 == 0:
#   print(f"{numero} es par") <-- Asi estaria bien
