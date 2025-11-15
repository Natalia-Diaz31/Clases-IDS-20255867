#vamos a procedera atender pedidos de pizza
#definir
def ordenar_pizza(size,masa, *ingredientes): #ahora con args conjunto de valores 
    """Vamos a imprimir su orden"""
    print(f"Usted ha ordenado una pizza {size} de masa {masa} de: ")
    for i in ingredientes:
        print(f"\t - {i}")
    
#llamar 
ordenar_pizza("grande","delgada", "tocino", "piña", "carne", "hongo")