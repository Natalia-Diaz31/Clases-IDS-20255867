A = int(input())
conteo = 0         

for _ in range(A):
    edad = int(input())
    if edad >= 15:
        conteo += 1

print(conteo)