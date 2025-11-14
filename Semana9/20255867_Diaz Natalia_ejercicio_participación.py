#Dui validación 
#condicoin 1 = largo 10 
#condicion 2 = tiene 1 - 
#condicion 3 = 1 caracter despues de _ 
#print cumple x condiciones

def dui_validacion(dui):
    condiciones = 0
    if len(dui) == 10:
        condiciones +=1
    if dui.count("-") == 1:
        condiciones += 1
    partes = dui.split("-")
    if len(partes) == 2 and len(partes[1]) == 1:
        condiciones += 1
    return condiciones

dui_ingresado = input("Ingrese su dui: ")
print(f"Cumple {dui_validacion(dui_ingresado)} condiciones")

    
    
