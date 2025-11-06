birthday = {
    "Alice": "Apr 1", 
    "Bob" : "Dec 12",
    "Carol" : "Mar4"
}
birthday["Carol"] = "Abr 21"
birthday["Fer"] = "Mar 3"

for persona, fecha in birthday.items():
    print(f"El cumpleaños de {persona} es en {fecha}")
    
del birthday["Bob"]
print(birthday)
print(birthday["Carol"])

