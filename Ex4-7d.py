Age = int(input("Entrez age: "))
Permis = int(input("Permis ancieneté: "))
NombreAccident = int(input("Entrez nombre accident: "))
AncieneteAssurance = int(input("Ancienete Assurance: "))
couleur = ""
malus = 0

if Age < 25:
    malus += 1

if Permis < 2:
    malus += 1

malus = malus + NombreAccident

if AncieneteAssurance > 5 and malus < 3:
    malus -= 1

match malus:
    case -1:
        couleur = "bleu"
    case 0:
        couleur = "vert"
    case 1:
        couleur = "orange"
    case 2:
        couleur = "rouge"
    case _:
        couleur = "refuse"

print("Le client est " + couleur)