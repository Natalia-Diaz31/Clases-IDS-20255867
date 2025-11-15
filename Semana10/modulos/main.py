#importar datos 
import funciones as fn
import datos as dt #todos los datos 
from datos import usuarios3 as u3 #una parte 

#orquetacion de modulos
fn.saludar_usuarios(dt.usuarios2)
fn.saludar_usuarios(u3)


fn.registro_profesores(
    "Rafa",
    "Orellana",
    ciclo1 = ["mate. Fin", "Simulacion", "progra"],
    ciclo2 = ["calculo5", "metodos"]
)

