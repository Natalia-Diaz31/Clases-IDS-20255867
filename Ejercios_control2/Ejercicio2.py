
"""2.	Utilizar listas.
Crear un lista con los cinco días laborales de la semana en español.
Por medio de inputs vamos a ir rellenando esta lista con la cantidad de 
productos vendidos para cada día. Luego de cada día actualizado, mostrar un mensaje, 
como por ejemplo “El día LUNES se vendieron 123 productos”
Calcule la cantidad total de productos de la semana.
"""
dias_laborales = ["lunes", "martes", "miercoles", "jueves", "viernes"]

lu = int(input())
ma = int(input())
mi = int(input())
ju = int(input())
vi = int(input())
print(f"El dia {dias_laborales[0].upper()} se vendieron {lu} productos")
print(f"El dia {dias_laborales[1].upper()} se vendieron {ma} productos")
print(f"El dia {dias_laborales[2].upper()} se vendieron {mi} productos")
print(f"El dia {dias_laborales[3].upper()} se vendieron {ju} productos")
print(f"El dia {dias_laborales[4].upper()} se vendieron {vi} productos")
costo_total = lu+ma+mi+ju+vi
print(f"El costo total fue de ${costo_total}")












"""
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
Lu = int(input("Lunes: "))
dias[0] = Lu #dias que antes era una lista ahora va a decir lo que se meta en el input
print(dias)

Ma = int(input("Martes: "))
dias[1] = Ma 
print(dias)

Mi = int(input("Miercoles: "))
dias[2]= Mi 
print(dias)

Ju = int(input("Jueves: "))
dias[3] = Ju
print(dias)

Vi = int(input("Viernes: "))
dias[4] = Vi 
print(dias)

print(f"la produccion de la semana fue {Lu+Ma+Mi+Ju+Vi}")
"""
