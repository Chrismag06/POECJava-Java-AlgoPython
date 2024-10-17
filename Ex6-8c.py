NombreValeur = int(input("Entrez un nombre de valeur "))
NombreNegatif = 0
NombrePositif = 0
NombreZero = 0
NombreNonDigit = 0
Valeur = 0

for i in range(1,NombreValeur + 1):
    Valeur = input("Entrez une valeur ")
    if Valeur.isdigit():
        match Valeur:
            case 0:
                NombreZero += 1
            case Valeur if Valeur > 0:
                NombrePositif += 1
            case Valeur if Valeur < 0:    
                NombreNegatif += 1
    else: 
        NombreNonDigit += 1

print(f"Nombre de valeur negatif {NombreNegatif}")
print(f"Nombre de valeur positif {NombrePositif}")
print(f"Nombre de valeur à zero {NombreZero}")
print(f"Nombre de valeur à NombreNonDigit {NombreNonDigit}")
