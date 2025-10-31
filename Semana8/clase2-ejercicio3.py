#un pequeño sistema de registro de alumnos 
#Configuración inicial 
"""
1- Agregar 
4- borrar 
3- modificar 
2- construir 
5- salir 
"""

alumnos = 0 
lista_alumnos = []
print("Bienevenido a nuestro sistema de control de Alumnos. ")

menu_activo = True
while menu_activo:
    opcion = input("Elija la opcion (1: Ingresar alumno, 5: Salir ")
    if opcion == "5":
        menu_activo = False
    elif opcion == "1":
        alumno = input("Nombre del alumno agregar: ")
        lista_alumnos.append(alumno)
    elif opcion == "2":
        print(lista_alumnos)
    elif opcion == "3":
        i = int(input("Ingrese la posicion del alumno a modificar: "))
        n = input("Ingrese el nuevo nombre del alumno")
        lista_alumnos[i-1] = n #por que empieza desde 0 
    elif opcion == "4":
        borrado = lista_alumnos.pop(int(input("Ingrese el numero del alumno a popear "))) 
        print(f"Ustedha popeado a {borrado}.")
    else:
        print("La opcion elegida no es valida.")
    
print("Gracias por utilizar nuestro sistema.")
        

