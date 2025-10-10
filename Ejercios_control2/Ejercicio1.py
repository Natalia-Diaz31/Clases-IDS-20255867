#Ejercicio 1 
"""Uso de Inputs y Casting
Vamos a capturar la cantidad de artículos producidos por mes y l
uego vamos a estimar el costo total. Para ello, vamos a recibir los 
meses de enero, febrero y marzo, y guardarlos en variables. 
Sabiendo que el costo de los artículos en enero fue de $1.25, 
en febrero fue de $1.38 y en marzo fue de $1.14. Calcule el costo total.
""" 

enero = int(input())
febrero = int(input())
marzo = int(input())

costo_total = enero*1.25 + febrero*1.38 + marzo*1.14

print(f"Su costo total fue de ${costo_total:.2f}")




"""#captura de cantidades 
Enero = int(input("Ingrese la cantidad de Enero: "))
Febrero = int(input("Ingrese la canidad de Febrero: "))
Marzo = int(input("Ingrese la cantidad de Marzo: "))

costo = Enero*1.25 + Febrero*1.38 + Marzo*1.14
print(costo)
print(f"Las cantidades de enero, febrero y marzo son:")
print(f"{Enero}, {Febrero} y {Marzo} con un costo")
print(f"de: {costo:.2f}")"""


