monto = float(input("Digite el monto"))
tipo = input("Tipo (local/internacional)")
impuesto = 0

if tipo.lower() == "local":
    if monto > 100:
        impuesto = 0.07
    else:
        if monto > 75:
            impuesto = 0.05
        else: 
            impuesto = 0 
            
elif tipo.lower() == "internacional":
    if monto > 100:
        impuesto = 0.12
    else: 
        if monto > 75:
            impuesto = 0.09
        else:
            impuesto = 0 
else: 
    print("Ese tipo no existe")
print(f"El tipo {tipo} con monto {monto:,.2f}")
print(f"paga un impuesto de {monto*impuesto:,.2f}")

"""
Iterable es cualquier coleccion sonbre la cual yo puedo llegar a realizar cualquiera de sus elementos: ejemplos: colecciones (string, lista, tupla)
Iterador es un eleeto sobre el cual o puedo hacer recorrido 
"""