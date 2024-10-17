Somme = int(input("Entrez une somme "))

TypeBillet = [100, 50, 20, 10, 5]

for t in TypeBillet:
    Reste = Somme % t
    print(f"Somme {Somme}")
    print(f"Nb billet {t} {int(Somme / 100)}")
    print(f"Reste {Reste}")
    Somme = Reste


