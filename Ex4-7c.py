Age = int(input("Entrez age: "))
Permis = int(input("Permis ancieneté: "))
NombreAccident = int(input("Entrez nombre accident: "))
AncieneteAssurance = int(input("Ancienete Assurance: "))

Contrat = "Refus"

if Age < 25 and Permis < 2 and NombreAccident == 0:
    Contrat = "Rouge"

if Age > 25 and Permis < 2 and NombreAccident == 0:
    Contrat = "Orange"

if Age > 25 and Permis < 2 and NombreAccident == 1:
    Contrat = "Rouge"   
        
if Age > 25 and Permis > 2  and NombreAccident == 0:
    if AncieneteAssurance > 5:
        Contrat = "bleu"
    else:
        Contrat = "Vert" 

if Age > 25 and Permis > 2  and NombreAccident == 1:
    if AncieneteAssurance > 5:
       Contrat = "Vert" 
    else:
        Contrat = "Orange"
     
if Age > 25 and Permis > 2  and NombreAccident == 2:
    if AncieneteAssurance > 5:
        Contrat = "Orange"
    else:
        Contrat = "Rouge"   

print(f"Contrat : {Contrat}")
    