# Los while loops se ejecutan infinitamente si la condicion se mantiene verdadera.


#while 1==1:
    #print("Esto es un loop")

nombre = ""

while len(nombre) == 0: # Hasta que la condicion no cambie de 0 me va a seguir solicitando el nombre (prueben apretando enter sin poner nada)
    nombre = input("Escribi tu nombre: ")


print (f"Hola {nombre}")




