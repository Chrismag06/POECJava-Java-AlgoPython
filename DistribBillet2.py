Somme = int(input("Entrez une somme "))

TypeBillet = {100, 50, 20, 10, 5}

for t in TypeBillet:
    Reste = Somme % t
    NbBillet = int(Somme / t)
    print(f"Nb billet 100 {NbBillet}")
    print(f"Reste {Reste}")








        
 
