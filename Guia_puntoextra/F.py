N = int(input())
for i in range(N):
    nombre = input().strip()
    longitud = len(nombre)

    if longitud <= 6:
        print("No vale la pena")
    elif longitud >= 8:
        print("Si aguanto otro desarrollo de personaje")
    else:
        print("Dios no creo aguantar esta vez")