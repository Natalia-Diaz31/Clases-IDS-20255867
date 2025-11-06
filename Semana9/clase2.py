#Enumera construir un correlativo al lado izquierdo 
surnames = ["Rivest","Shamir","Adleman"]
for position, surname in enumerate (surnames): #enumarate genera una lista 
    print(position, surname)
    
#Zip va a evaluar lstas juntas 
people = ["Nick", "Rick", "Roger", "Syd"]
ages = [23,24,23,21]
instruments = ["Drums","Keyboards","Bass","Guitar"]
for person, age , instrument in zip(people,ages, instruments):
    print(person,age, instrument)
    #toma el largo menor de las listas 