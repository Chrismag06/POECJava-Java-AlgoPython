Somme = int(input("Entrez une somme "))

billetCent = 0
billetCinquante = 0
billetVingt = 0
billetDix = 0
billetCinq = 0

if Somme % 5 == 0:
    while Somme > 0:
        if Somme >= 100:
            Somme -= 100
            billetCent += 1
        elif Somme >= 50:
            Somme -= 50
            billetCinquante += 1
        elif Somme >= 20:
            Somme -= 20
            billetVingt += 1
        elif Somme >= 10:
            Somme -= 10
            billetDix += 1
        elif Somme >= 5:
            Somme -= 5
            billetCinq += 1

    if billetCent != 0:
        print(f"Billet Cent {billetCent}")
    if billetCinquante != 0:
        print(f"Billet Cinquante {billetCinquante}")
    if billetCent != 0:
        print(f"Billet Vingt {billetVingt}")
    if billetCent != 0:
        print(f"Billet Dix {billetDix}")
    if billetCent != 0:
        print(f"Billet Cinq {billetCinq}")

else:
    print("c'est pas correct")

