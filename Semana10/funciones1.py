#este modulo va a contener funciones 

#un afuncion tiene 2 tiempos, una definicion y una llamada

#definir
def mi_funcion(): #dentro de ls parentesis son los parametros 
    print("Hola mundo")
    print("amigo usuario")
    print("gracias por usar nuestro sistema!")
    
mi_funcion() #puedo poner argumentos 

#rcibir informacion desde afuera de la funcion 
def capturar_nombre():
    """Esta funcio recibe valores por medio de input"""
    nombre_input = input("Escriba su nombre: ")
    apellido_input = input("Ecriba su apellido: ")
    nombre_completo= f"{nombre_input.capitalize()} {apellido_input.capitalize()}"
    print(nombre_completo)
  
def capturar_usuario(nombre,edad) :
    nombre_usuario = nombre
    edad_usuario = edad
    texto = f"El usuario {nombre_usuario.title()} tiene {edad_usuario} años de edad" 
    print(texto)
    
#llamadando funcion capturar_nombre
capturar_nombre()
capturar_usuario(input("Ingrese su nombre: "), input("Edad: "))


#calculo de impuesto 
def calculo_impuesto(ventas):
    """Esta funcion calcula el valor del impuesto"""
    if ventas < 500:
        tasa_impuesto = 0.1
    else:
        tasa_impuesto = 0.25
    return tasa_impuesto

ventas = 1000
print(f"""el valor de la venta fiue de {ventas},
      la tasa de impuesto es {calculo_impuesto(ventas)},
      y el monto por tanto es ${calculo_impuesto(ventas)*ventas:,.2f}""")