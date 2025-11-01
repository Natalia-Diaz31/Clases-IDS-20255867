#1. Configuración inicial 
agente = "encargado" 
platillo = [] #lista donde seran ingresados los futuros datos 
precios = []
#2. Ingreso a la aplicación 
nombre_agente = input("Ingrese el nombre del agente: ") #no le puse punto lower, por que es como uan contraseña para mi entonces tiene que ser justo tal cual como esta escrita
while nombre_agente != agente: #aqui si el nombre del agente no es correcto, no lo deje entrar y mostrara el mensaje siguiente.
    print("Agente no registrado.")
    nombre_agente = input("Favor ingrese el nombre del agente: ")
print("Bienvenido") #cuando si lo ponga correcto sera bienvenido :)
#3. Gestión del menú principal 
estado = True  #comenzar mi bucle 
while estado:
    print("1. Creación de platillos") #Las opciones, las puse asi para que no se vea todo desordenado en una sola linea
    print("2. Consulta de platillos y precios")
    print("3. Colocar un pedido")
    print("4. Salir")
    elegir = int(input("Ingrese el numero de opcion: ")) #que me de la opcion que quiere ejecutar.
#4. Creación de platillos 
    if elegir == 1: # aqui es si la persona elige X(numero de opcion) se va a ejecutar es parte en especifico.
        nombre_platillo = input("Ingrese el nombre del platillo a crear: ").lower() #que ingrese los datos que se le piden, le puse .lower() para que asi cuando se quiera buscar no sea dificil y no afecte el como la escriban. 
        precio_platillo = float(input("Ingrese el precio del platillo a crear: ")) 
        platillo.append(nombre_platillo) #los datos que se ingresaron previamente se agregaran a la lista que hice al principio. 
        precios.append(precio_platillo)
#5. Consulta de platillos 
    elif elegir == 2:
        if len(platillo) == 0: #si no hay inguna información (lista vacia) se le informara. 
            print("Actualmente no hay platillos ingresados") 
        else: 
            for i in range(len(platillo)): #si no ,se va a ejecutar la busqueda del platito, podra verficiar los datos.
                print(f"{platillo[i]}: ${precios[i]:.2f}") #y se va a mostrar el resultado por medio de una oracion. 
#6. Colocar un pedido 
    elif elegir == 3:
        if len(platillo) == 0: #aqui nuevamente le puse que si no habia informacion que lo dijera. 
            print("No hay plato disponible") 
        else:
            pedido = input("Indique el nombre del platillo para su orden: ").lower() #pido el plato a evaluar es punto lower para que no haya problema entre mayusculas y minusculas y que por eso no me encuentre el plato.
            if pedido in platillo: #si lo que dice esta en la lista :)
                pedidito = platillo.index(pedido) #me da el plato que eligio 
                print(f"Usted ha elegido {pedido} con un precio de ${precios[pedidito]:,.2f}") #me lo muestra en una oración bonita
            else:
                print("El plato ingresado no existe") #si hay informacion en la lista pero la opcion del plato que puso no esta, se le dira tambien que no esta esa informacion. 
#7. Salir
    elif elegir == 4:
        estado = False #aqui es para que bucle se cierre y finalice :)
        print("Termino") #:3 Termino el codigo 
        

    
    

    
