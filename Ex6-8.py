NombreValeur = int(input("Entrez un nombre de valeur "))
NombreNegatif = 0
NombrePositif = 0

for i in range(1,NombreValeur + 1):
    if int(input("Entrez une valeur ")) >= 0:
        NombrePositif += 1
    else:
        NombreNegatif += 1

print(f"Nombre de valeur negatif {NombreNegatif}")
print(f"Nombre de valeur positif {NombrePositif}")
