Nombre = "Alvin"
Palabra = "RECONOCER"
otra_palabra = "palabra"

print(len(Nombre)) #imprime el largo de la cadena de caracteres 
print(Nombre[2]) #extraer un componente o caracter de la cadena
print(Nombre[2:5]) #se debe de poner 1 mas por que no incluye el ultimo en este caso seria N que es el 4
#[2:5[ (se esvribe asi [] pero se interpreta [[)
#RECONOCER (palindromos, palabras que se leen igual al reves y derecho)
print(Nombre[2:4])
print(Nombre[2:]) #si no se pone nada le estamos diciendo que desde el incio hasta el ultimo 

###################################################

print(len(Palabra))
print(Palabra[4:8]) #quinto caracter hasta la E
print(Palabra[0:9:2]) #inicio:final:salto aqui saco solo las consonantes 
print(Palabra[1::2]) #aqui solo saco las vocales 
print(Palabra[::2]) #aqui le digo que desde el principio hasta el final en salto de 2 
print(Palabra[::-1]) #aqui le digo que me lo imprima al reves """

print(len(Palabra))
print(Palabra[::-1])
print(otra_palabra[::-1]) #aqui me la escribe al reves 

Palabra = "roma ni se conoce sin oro ni se conoce sin amor"
print(Palabra[::-1])
print(Palabra == Palabra [::-1]) #si me preguntan si es palindromo o no hago esto, aqui compara si palabra es igual a palabra al reves , recuerda que == es comparación


#############################

numero = "255" #con las "" lo hacemos cadena de texto 
print(numero)
print(len(numero)) #aqui me da error por que numero no es una cadena de caracteres y los numero no tiene largo, los textos si. en string no hay cadena de numeros, solo son numeros 
#cuando estoy creadno el objeto ya reconoce si es texto o numero, si es texto le puedo sacar el largo, si es numero no le puedo sacar el largo

mi_palabra = "jocote de corona"
print(mi_palabra)
mi_palabra_mayuscula = mi_palabra.upper()
mi_palabra_cap = mi_palabra.capitalize()
print(mi_palabra_mayuscula)
print(mi_palabra_cap)


