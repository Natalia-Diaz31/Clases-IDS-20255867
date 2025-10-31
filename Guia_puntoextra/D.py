N = int(input())
numeros = []

for i in range(N):
    num =  int(input())
    numeros.append(num)
    
contar_7 = numeros.count(7)
contar_5 = numeros.count(5)


print(contar_7, contar_5)
    