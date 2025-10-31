"""
Condicionales: 
IF 
componentes:if,else,elif

Bucles:Finito(for),coleccion (sttring,lista,tupla,dict), que haga una accion por una cantidad finita de veces
e infinito ()

"""
palabra = "Hola"
#print(len(palabra))

lista = [10,11,12,13,14]
#print(len(lista))
dias = ["Lunes","Martes","Miercoles",
        "Jueves","Viernes","Sabado","Domingo"]
#print(len(dias))

#for i in dias: #va a repetir segun elementos de la coleccion; i = interador() ; dias = iterable (la coleccion que contiene los iteradores )
#    print(i) #imprima los elementos 
    
#Auixiliar RANGE(inicial,final)

for i in range(5): #quiero que me imprimi un rango de valores desde el 0 hasta el 5 sin incluir el 5 
    print("Buenos dias")
    
for i in dias[3]:
    print(i)

valores = [[1,3,6],
           [2,7,4],
           [6,5,9],
           [1,10,20]]
mayores = [] # mayores va a comenzar como una lista vacia 
for v in valores: #v son las filas 
    for i in v: #elementos de v 
        if i >6:
            mayores.append(i)
print(mayores)

#Ejercicio 
dias = "Lunes", "Martes", "Miercoles", "Jueves", "Viernes"
Ana = 8, 8, 9, 8, 10 
Luis = 7, 9, 10, 8, 7
Juan = 7, 8, 8, 8, 8
Maria = 8, 8, 10, 7, 11

