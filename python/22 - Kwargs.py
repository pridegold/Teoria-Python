# kwargs Acumula argumentos en dicccionarios, a diferencia de args
# Util para que una funcion pueda acepte una cantidad variada de argumentos tipo keyword

def hola (**kwargs):
  print("Hola",end=" ") # Prueben sacando el ,end= " " y van a ver como lo que se printea se hace de una forma poco ortodoxa
  for key,value in kwargs.items():
    print(value,end=" ")

hola(primero="Damian", medio="Ariel", segundo="Lopez")