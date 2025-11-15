#vamos a crear una funcion utilizando kwargs 
#args listas *
#kwargs diccionarios **

def registro_profesores(nombre,apellido, **materias):
    """Crear un registro de profesor, utilizanod kwargs"""
    print(f"El profesor {nombre} {apellido} imparte las materias: ")
    for ciclo, materias in materias.items():
        print(f"\t - {ciclo}: \t {materias}")
        
    registro_profesores(
        "Alvin",
        "Portillo",
        Ciclo1 = ["BD1", "IIJ","A&D"],
        Ciclo2 = ["DAI", "BD2", "SINE"],
        Ciclo3 = ["IDS", "FPEN", "PAD"]
    )