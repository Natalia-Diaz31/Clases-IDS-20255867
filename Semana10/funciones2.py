def registrar_usuarios(nombre, apellido, inicial= " ", edad = 0 ): #losparametros qu etienen un valor por defecto van hasta el final, primero los obligatorios van al incio, 
    """Construir in nombre a partir de sus componentes"""
    if edad: 
        texto_completo = f"La persona {nombre} {inicial} {apellido}, de {edad} años de vida."
    else:
        texto_completo = f"La persona {nombre} {inicial} {apellido}."
        
    return texto_completo
print(registrar_usuarios("Daniel","Wisecarver"))

#una funcion que es usadapor una lista 

def saludar_usuarios(nombres):
    """Saludar usuario"""
    for nombre in nombres:
        print(f"Hola, {nombre.capitalize()}")
    
usuarios = ["Ana", "Luis", "Juan"]
saludar_usuarios(usuarios)

