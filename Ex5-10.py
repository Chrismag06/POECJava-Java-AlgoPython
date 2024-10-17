Prix = -1
Somme = 0

while Prix != 0:
    Prix = int(input("Entrez un prix et zero pour terminer "))
    Somme += Prix

print("Somme ", "{:.2f}".format(Somme))

Paiment = int(input("Entrez un paiement : "))

Monaie = Paiment - Somme
billet10 = int(Monaie / 10)
print(f" Monaie rendu ")
print(f" billet 10 : {billet10}")

Monaie = Monaie % 10
billet5 = int(Monaie / 5)
print(f" billet 5 : {billet5}")

Monaie = Monaie % 5
print(f" billet 1 : {Monaie}")