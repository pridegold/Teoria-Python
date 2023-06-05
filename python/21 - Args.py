# args es un parametro que juntara todos los argumentos en una tupla
# Es util para que una funcion pueda aceptar una cantidad variada de argumentos

#def agregar(n1, n2):
  #sum = n1 + n2
  #return sum

#print(agregar(1,2,3)) # Esto arrojaria error ya que estoy pasando 3 argumentos y la funcion solo permite 2

def suma(*args):
  resultado = sum(args)
  print(resultado)


suma(3,4,6)
suma(3,4,7)