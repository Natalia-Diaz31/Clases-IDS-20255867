"""4.Utilizar tuplas.
Vamos a crear una colección de los nombres de 7 alumnos, 
en el orden en el que ingresaron al aula.
Ingresaremos el número en el orden en el cual ingresaron,
y nos debería indicar esa posición y el nombre del alumno. 
Por ejemplo , “El alumno que ingreso como número 2 es Pedro”.
"""
alumnos = ("Diego", "Franquito", "Calvito", "Aby", "Alvin", "Medranito","Jessiquita")
ninio = int(input("Ingrese el orden del niño que desea saber (1-7): "))
print(f"El alumnno que ingreso como numero {ninio} es {alumnos[ninio-1]}") #por que python empieza a contar desde 0 entonces para no explicar eso se pone -1 

