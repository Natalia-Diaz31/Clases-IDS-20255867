#Listas 
"""Permiten principalmente guardar valores y son mutableses
Agrupan valores em corchetes
es heterogeneos
colecciones
son objetos y todos los objetos tiene propiedades y metodos(que son funciones)"""
datos = [1,2,"tres",["lunes","martes","miercoles"]] #tenemos 3 colecciones la primera son los datos, la segunda son las ltras y la tercera es una lista 
print(datos) #1,2,"tres"
print(datos[2])#tres
#print(datos[2[1]]) no funciona, no se mete corchete entre corchete 
print(datos[3][2][3]) #forma correcta 

#Concatenar listas 
numeros = ["uno","dos","tres"] 
print(numeros)
numeros = numeros + ["cuatro","cinco","seis"]
print(numeros)
print(len(numeros))
numeros[2] = "trois"
print(numeros)
numeros.append(input("Escriba el siguiente numero: ")) #agregarle un valoral final 
print(numeros)
numeros.insert(2,"Einender nummer: ")#en que posicion voy agregar que valor 
print(numeros)
