# Exepciones son eventos que se detectan al interrumpir la fluidez de un programa



#numerador = int(input("Colocar numero para dividir: "))
#denominador = int(input("Colocar numero para dividir por: "))
#resultado = numerador / denominador # si coloco cualquier numero int dividido 0, el programa daria error matematico
#print(int(resultado)) 

# Entonces encerremos nuestro programa primero intentando el mismo mediante Try y ejecutando la excepcion

try:
    numerador = int(input("Colocar numero para dividir: "))
    denominador = int(input("Colocar numero para dividir por: "))
    resultado = numerador / denominador # si coloco cualquier numero int dividido 0, el programa daria error matematico
     
# El error que nos arrojaba al dividir por 0, es el que tenemos que copiar para exceptuarlo
except ZeroDivisionError:
    print("No se puede dividir por 0")
# Podemos indicar que solo coloque numeros
except ValueError:
    print("Solo ingrese numeros porfavor")
except Exception:
    print("Algo salio mal")

else:
    print(resultado)

finally:
    print("Esto siempre se va a ejecutar")