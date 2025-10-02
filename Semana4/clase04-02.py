cantidad_alumnos = 25 
nombre_profe = "Alvin"
nuevas_inscripciones = 0 
nombre_profe = input("Ingrese el nombre del profesor: ")
nuevas_inscripciones = input("Nuevos alumnos: ")
nuevas_inscripciones = int(nuevas_inscripciones) #convierto el str a int


print(type(nombre_profe))
print(nombre_profe)
print(cantidad_alumnos + nuevas_inscripciones) #esto da error porque no se pueden sumar un int con un str
print(cantidad_alumnos + int(nuevas_inscripciones)) #con el int convierto el str a int para poder sumar
