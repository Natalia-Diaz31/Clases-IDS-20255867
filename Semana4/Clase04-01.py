"""usuario = "Natalia" #Tipo string 
cantidad_alumnos = 74 
media_edad=18.238134
monto_hope = 123456765.676
inversion_evento = -9886556

print(type(cantidad_alumnos)) 
print(type(media_edad))

print(type(cantidad_alumnos) is int) #no es lo mismo "int" que int con comillas es tipo texto mientras que sin es la funcion el tipo de dato 
print(type(media_edad) is int) 

print("el usuario es", usuario, "y tiene", cantidad_alumnos, "pajaritos en su aula")
print ("y la edad promedio es", media_edad)

#stringf (es texto formateado), los texto que van despues de la f tiene la capaciad de aceptar formatos y tomar variables dentro de el. los {} me dan la posibilidad de hacer cosas que un texto plano no haria 
print(f"El usuario es {usuario}")
print(f"y su aula con {cantidad_alumnos-4} pajaritos en su aula")
print(f"y la edad promedio es {media_edad:.2f} años") #el .2f me permite limitar a 2 decimales
print(f"colectaron {monto_hope:,.2f} como un donativo") #el , me permite poner el separador de miles
print(f"y la totalidad de gastos fue de ${abs(inversion_evento)} dolares")#el abs me permite convertir un numero negativo en positivo

print(type(usuario) is str)

#booleans (true- falso)

esta_lloviendo = False
print(type(esta_lloviendo) is not bool) #el not me permite negar la condicion
print(type(esta_lloviendo) is bool) 
"""

#cadenas de texto (str)
nombre = "Natalia"
apellido = "Diaz"
nombre_completo = nombre + " " + apellido #el espacio entre comillas es para que haya un espacio entre los nombres
print(nombre_completo)



