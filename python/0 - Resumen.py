# Escribir
print("Hola")
# Colocar un string
nombre = input("Coloca tu nombre: ")
print(f"Hola {nombre}", end=" ")
# Colocar un int
n1 = int(input("Coloca otro numero: "))
print(f"Tu numero es {n1}")
# While loops
n2 = int(input("Ingresa otro numero: "))
while True:
    
    if n2 % 2 == 0:
        print(f"{n2} es par")
        break
    else:
        print(f"{n2} es impar")
    break
# For Loops
for x in range(0,102):
    if x % 2 == 0:
        print(x)

# String slicing
id = "Lucas Gonzalez"
nombre = id[0:5]
apellido = id[6:]
print(f"Hola {nombre} {apellido}")

id2 = "Lucas Gonzalez 13.599.610"
dni = id2[14:]
slice = slice(0,14)
print(id2[slice], (dni))

#Listas [] Ordenados
comida = ["pizza","empanada","tarta"]
comida.append("sushi")
comida.insert(2, "langostino")
comida.sort()
print(comida)  

# Sets {} No ordenados
pc = {"cpu", "mouse", "teclado"}
marcas = {"logitech","steelseries","razer"}

pc.add("Mesa")
pc.remove("mouse")
pc.update(marcas) # Ahora Pc contiene todos los valores
Proovedor = pc.union(marcas)
#print(Proovedor)
print(marcas.difference(pc)) # aparecera un set vacio, ya que no tienen diferencia por que PC contiene todo
print(marcas.intersection(pc)) # Aparecen solo el contenido de marcas

# Diccionarios {}

Precios = {"GTX1050": "150000",
           "GTX1060": "180000",
           "GTX1070": "210000",
           "GTX1080": "300000"
           }

#print(Precios.keys()) Ver llaves
#print(Precios.values()) Ver Valores
#print(Precios.items()) Ver llaves y valores

Precios.update({"GTX1050":"151000"})


for key, value in Precios.items():
    print(key, value)

print(Precios.get("GTX1080"))
















