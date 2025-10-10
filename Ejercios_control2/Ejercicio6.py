"""6.Utilizar métodos de string
Se le pedirá al usuario que ingrese su salario, en esta oportunidad 
puede incluir el símbolo de dólar ($). Cuando este texto sea ingresado, 
se deberán validar dos condiciones (por separado) indicando su resultado 
por medio de un mensaje que incluya el boolean TRUE/FALSE.
a)	Que cuente con UN símbolo de dólar
b)	Que cuente con símbolo de dólar al INICIO del texto.
"""
salario = (input("Ingrese su salario: "))
print(salario[0]=="$")
print(salario.count("$")==1)


