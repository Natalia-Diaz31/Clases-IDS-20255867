#voy a iniciar mi variale en True 
ejecucion = True 

while ejecucion:
    opcion = input("Estamos ejecutando el mendu? Y/N: ")
    if opcion.lower() == "n":
        ejecucion = False 
    elif opcion.lower() == "y":
        print("Ok, continuemos")
    else:
        print("La opcion elegida no es valida")
        
print("Gracias por utilizar nuestro sistema!!!")



    