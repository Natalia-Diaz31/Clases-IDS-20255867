#Ejercicios de Tuplas 

Tupla1 = (1,12,255,1289,60,000) #es inmutable 
Lista = [1,12,255,1289,60,000] #las listas van en [] y es mutable 

#los dos usan indices para recuperar elementos

print(len(Tupla1))
print(Tupla1[4]) #aqui me imprime el quinto elemento de la tupla, es decir recuperar un elemento 
print(Tupla1[3:]) 

#print(Tupla1[-1]) #el -1 es para recuperar el ultimo elemento (contar de derecha a izquierda)
##print(Tupla1) #me dio error pero no se les llama errores se les llama excepciones 

Lista[-1] = 3 
print(Lista) #aqui si me lo cambio por que las listas son mutables

