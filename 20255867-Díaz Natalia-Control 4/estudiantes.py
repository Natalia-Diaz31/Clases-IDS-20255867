#2. REGISTRAR ESTUDIANTE 
def registrar_estudiante(lista_estudiantes): #la funcion principal 
    nombre = input("Ingrese su nombre: ")
    carnet = "S" + str(len(lista_estudiantes) + 1).zfill(3) #genero el carnet
    
    estudiante = {  #aqui cree mi diccionario de estudiante 
        "carnet": carnet.upper(),
        "nombre": nombre.title()
    }
    lista_estudiantes.append(estudiante) #guardo el estudiante 
    print(f"El estudiante {nombre.title()} con carnet {carnet} fue registrado :)")
    
# 5. MOSTRAR ESTUDIANTE 
def mostrar_estudiantes(lista_estudiantes):
    if len(lista_estudiantes) == 0: #primero le digo al usuario si hay o no estudiantes 
        print("No hay estudiantes :(")
        return
    for estudiante in lista_estudiantes: #muestro todos los estudiantitos 
        print(f"Estudiante: {estudiante['nombre']} con carnet: {estudiante['carnet']}")

