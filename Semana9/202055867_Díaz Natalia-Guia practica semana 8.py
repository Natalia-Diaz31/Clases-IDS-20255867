clientes = []
productos = []
pedidos = []

estado = True 
while estado:
    print("1. Mostrar productos") 
    print("2. Agregar Productos")
    print("3. Registrar nuevo cliente")
    print("4. Mostrar clientes")
    print("5. Registrar pedidos") 
    print("6. Mostrar pedidos del día")
    print("7. Mostrar categorías disponibles")
    print("8. Salir")

    elegir = int(input("Ingrese el número de opción: ")) 

    # 1. Mostrar productos 
    if elegir == 1: 
        if len(productos) == 0:
            print("No hay productos")
        else:
            for i, p in enumerate(productos):
                print(f"{i+1}. {p["codigo"]} {p["nombre"]} {p["categoria"]} ${p["precio"]:,.2f}")
    # 2. Agregar Productos
    elif elegir == 2:
        codigo = "P" + str(len(productos)+1).zfill(3)
        nombre =input()
        categoria = input()
        precio = float(input())
        nuevecito = print(f"{i+1}. {p["codigo"]} {p["nombre"]} {p["categoria"]} ${p["precio"]:,.2f}")
        productos.append(nuevecito)
    # 3. Registrar nuevo cliente 
    elif elegir == 3:
        codigo_cliente = "C" + str(len(clientes)+1).zfill(3)
        nombre_cliente = input()
        telefono = int(input())
        clientesito = {"codigo": codigo_cliente, "nombre": nombre_cliente, "telefono": telefono}
        clientes.append(clientesito)
    # 8. Salir
    elif elegir == 8:
        print("Adiosito")
        estado = False  


    