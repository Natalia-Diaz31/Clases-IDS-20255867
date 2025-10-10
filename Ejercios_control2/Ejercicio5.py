"""5.	Utilizar métodos de strings.
Vamos a capturar nombre y apellido por medio de inputs, y a partir de ello, 
usted que trabaja para la empresa ISND, se le pide que construya DOS propuestas de 
correo a partir de los datos ingresados. Por ejemplo, si la persona (incluyendo errores) 
escribe que sus nombres son JuaN TorrEs, el programa deberá indicar:

“Propuesta 1: juan.torres@ISND.com”
“Propuesta 2: jtorres@ISND.com”"""


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nombre_minus = nombre.lower()
apellido_minus = apellido.lower()

print(f"{nombre_minus}{apellido_minus}@ISND.com")
print(f"{nombre_minus[0]}{apellido_minus}@ISND.com")

