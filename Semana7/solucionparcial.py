#resolución del parcial 
#A
num1 = input()
num2 = input()
print(num1==num2)
#B 
nume1= int(input())
nume2 = int(input())
print(nume1 % nume2 == 0)
#C 
palabra = input()
letra = input()
print (palabra[-1].lower() == letra.lower())
#D 
palabrita = input()
print(palabrita[::-1].lower() == palabrita.lower())
#E
"""Los errores entran en categorias
excepciones TRACEBACK es decir errores
Se tiene que pensar en los errores y encapsularlos 
errores que puedo llegar a controlar"""
phrase = input()
letter = input()
print(letter in phrase)
#F
number = float(input())
print(number == int(number))
#G
dui = input()
cond1 = len(dui) == 10 
cond2 = dui[8] == "-"
cond3 = type(int(dui[-1])) is int()
#El valor no es lo mismo que el tipo 





