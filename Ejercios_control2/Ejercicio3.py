"""Utilizar listas.
Crear una lista llamada frutas, donde vamos a colocar la fruta favorita de 6 niños que 
vamos a ir llamando. Estos niños serán llamados en orden aleatorio. Originalmente esta 
lista tendrá los valores uno, dos, …, seis.
Crear una consulta de 6 peticiones para que cada niño mencione cuál es su fruta favorita. 
Luego de cada petición, mostrar la lista actualizada.
"""
frutas = ["uno", "dos", "tres", "cuatro", "cinco", "seis"]

favorita = input()
frutas[0] = favorita
print(frutas)

favorita = input()
frutas[1] = favorita
print(frutas)

favorita = input()
frutas[2] = favorita
print(frutas)

favorita = input()
frutas[3] = favorita
print(frutas)

favorita = input()
frutas[4] = favorita
print(frutas)

favorita = input()
frutas[5] = favorita
print(frutas)
