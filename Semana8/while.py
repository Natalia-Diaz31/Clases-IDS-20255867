limite = 8 
inicio = 0 

while inicio < limite:
    print(inicio)
    inicio = inicio + 1
    
    
    presupuesto = 1000
    gasto = 0 
    while gasto < presupuesto:
        compra = float(input("Monto a comprar: "))
        gasto += compra
    gasto -= compra 
    print("Ha llegado al limite de presupueso")
    print(f"El monto gastado es de {gasto:,.2f}")
    
    
    