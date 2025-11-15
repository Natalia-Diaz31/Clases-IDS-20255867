#3. REGISTRAR PRÉSTAMO
def registrar_prestamo(lista_libros, lista_estudiantes, lista_prestamos):
    carnet = input("Ingrese el carnet del estudiante: ").upper()
    
    estudiante_existe = False  #Aqui estoy verificando si el estudiante con el codigo que metio existe , primero asumo qu eno existe hasta que verifique 
    for estudiante in lista_estudiantes: #recorro la lista 
        if estudiante["carnet"] == carnet: #compararo el carnet con los de la lista 
            estudiante_existe = True #si si esta digo que sipii, existe 
            break #ya lo encontre asi que ya no sigo :3
    
    if not estudiante_existe: #en caso no lo encuentro pues les digo :(
        print("Ese estudiante no existe :(")
        return

    codigo = input("Ingrese el código del libro: ").upper()

    libro_existe = False  #Veo si el libro existe o si no y asumo que no existe :)
    for libro in lista_libros:#recorro la listita 
        if libro["codigo"] == codigo: #similar a la logica que utilice en estudiate comparo lo que me dieron con la info de la lista 
            libro_existe = True #si lo encontre digo que sipiii si existe 
            libro_encontrado = libro  #guardo el libro que encontré
            break

    if not libro_existe: #si no lo encuentro bueno :( les digo
        print("El libro no existe :(")
        return

    if libro_encontrado["disponible"] == False:  #Veo si el librito esta prestado o si aun sigue vigente 
        print("Ese libro ya fue prestado :(") #si ya sale que fue prestado doy el mensajito 
        return

    # Si llegamos hasta aquí, sí se puede prestar :)
    fecha = input("Fecha del préstamo (AAAA-MM-DD): ")

    prestamo = {
        "carnet": carnet,
        "codigo_libro": codigo,
        "fecha": fecha
    }

    lista_prestamos.append(prestamo)
    libro_encontrado["disponible"] = False  #el librito ya no está disponible

    print(f"Préstamo registrado: {carnet} pidió el libro {codigo} el día {fecha} :)")


#6. MOSTRAR PRÉSTAMOS
def mostrar_prestamos(lista_prestamos):
    if len(lista_prestamos) == 0: #si no hay prestamo me va a decir que no hay 
        print("No hay préstamos")
        return

    for prestamo in lista_prestamos: #aqui me va a mostrar si hay 
        print(f"El estudiante {prestamo['carnet']} tiene el libro {prestamo['codigo_libro']} desde {prestamo['fecha']}.")

        