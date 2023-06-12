# Las tuplas son colecciones ordenadas y que no pueden ser cambiadas, usadas para agrupar data relacionada

# Para formar tuplas los valores de la variable van con ()
estudiante = ("Damian", 25, "hombre") 

print(estudiante.count("Damian")) # Cuantas veces aparece el valor que buscamos
print(estudiante.index("hombre")) # En que index se encuentra el valor que buscamos

for x in estudiante: # Printear los valores de la tupla
    print(x)


if "Damian" in estudiante:
    print("Damian esta aca! ")     