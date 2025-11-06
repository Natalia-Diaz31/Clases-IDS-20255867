semana = {}
semana["uno"] = "Lunes"
semana["dos"] = "Martes"
semana["tres"]= "Miercoles"
semana["cuatro"] = "Jueves"

print(semana)

for v in semana.values():
    print(v)
    
for k, v in semana.items():
    print(f"El dia {k} ")