# Clave valor
# La clave es un índice que no se puede repetir.
dic = {}
edades = {
    "Juan": 67,
    "Maria": 76
}

edades["Maria"] = 33
edades["Arturo"] = 67

# Método get (mas seguro)
print(edades.get("Besay", "Por añadir"))

# Iterar diccionarios
for nombre, edad in edades.items():
    print(f"{nombre} tiene {edad} años")