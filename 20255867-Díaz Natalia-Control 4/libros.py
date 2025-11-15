#1. REGISTRAR LIBRO 
def registrar_libro(lista_libros): #la funcion principal :)
    titulo = input("Titulo: ") #aqui pido la información 
    autor = input("Autor: ")
    codigo = "L" + str(len(lista_libros)+ 1).zfill(3) #genero el codigo unico y uso zfill pata rellenar el codigo
    
    libro = { # mi diccionario 
        "codigo": codigo.upper(), 
        "titulo": titulo.title(),
        "autor": autor.title(),
        "disponible" : True #marco l libro como disponible 
    }
    
    lista_libros.append(libro) #guardar el nuevo libro 
    print(f"El libro {titulo.title()} de {autor.title()} con codigo {codigo.upper()} fue registrado :)")

#4. MOSTRAR LIBRO 
def mostrar_libros(lista_libros):
    if len(lista_libros) == 0: #primero reviso si hay libritos 
        print("No hay libritos")
        return
    for libro in lista_libros: #si si hay los voy mostrando 
        estado = "Disponible" if libro["disponible"] else "Prestado"
        print(f"El libro {libro['codigo']} {libro['titulo']} de {libro['autor']} está {estado}") #muestro el librito 
        