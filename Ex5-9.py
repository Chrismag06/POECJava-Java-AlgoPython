NombreMax = 0
Nombre = -1

while Nombre != 0:
    Nombre = int(input("Entrez un nombre et zero pour terminer "))
    if NombreMax < Nombre:
        NombreMax = Nombre
    
print(f"Nombre max est : {NombreMax}")