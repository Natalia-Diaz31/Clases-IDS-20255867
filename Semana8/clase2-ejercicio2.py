#un pequeño sistema de registro de alumnos 
#Configuración inicial 
alumnos = 0 
lista_alumnos = []
cantidad = int(input("Cuantos alumnos vamos a ingresar? ")) #mi rango para saber cuantos nombres voy a meter

for i in range (cantidad):
    alumno = input("Digite el nombre del pajarito: ")
    lista_alumnos.append(alumno) 

print(lista_alumnos)



