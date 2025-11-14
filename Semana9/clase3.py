#Este es un docstring de modulo 
#vamos a crear varias funciones 
#una funcion tiene dos momentos cuando se define y cuando se llama

def saludar():
    nombre = input("Digite el nombre: ")
    apellido = input("Digite su apellido: ")
    nombre_completo = f"{nombre.upper()} {apellido.upper()}" #title es para que la primer letra sea mayuscula
    print(f"Hola {nombre_completo}") #crear una funcion para luego solo llamarla 
saludar()


def saludar_parametro(nombre, apellido):
    
    print(f"Hola {nombre.title()} {apellido.title()}")

saludar_parametro("Fer", "Calvo")
saludar_parametro("FRANCO","ROSALES")

def describir_mascota(animal, nombre_mascota):
    """Vamos a describir mascotas"""
    print(f"Tengo un {animal}, y su nombre es {nombre_mascota}")
describir_mascota(nombre_mascota="firulais",animal="perro")
describir_mascota("gato","mishito")       
describir_mascota(
    input("Digite el tipo de animal: "),
    input("Digite el nombre de la mascota: ")
)       
