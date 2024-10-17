Age = int(input("Entrez age: "))
Permis = int(input("Permis ancieneté: "))
NombreAccident = int(input("Entrez nombre accident: "))
AncieneteAssurance = int(input("Ancienete Assurance: "))

if Age < 25 and Permis < 2 and NombreAccident > 0:
    Contrat = "Refus"

if Age < 25 and Permis < 2 and NombreAccident == 0:
    Contrat = "Rouge"

if Age > 25 and Permis < 2:
    if NombreAccident == 0:
        Contrat = "Orange"
    elif NombreAccident == 1:
        Contrat = "Rouge"
    else:
        Contrat = "Refus"       
        
if Age > 25 and Permis > 2:
    if NombreAccident == 0:
        Contrat = "Vert"
    elif NombreAccident == 1:
        Contrat = "Orange"
    elif NombreAccident == 2:
        Contrat = "Rouge"
    else:
        Contrat = "Refus"

if AncieneteAssurance > 5:
    if Contrat == "Vert":
        Contrat = "bleu"
    elif Contrat == "Orange":
        Contrat = "Vert"
    elif Contrat == "Rouge":
        Contrat = "Orange"

print(f"Contrat : {Contrat}")
    