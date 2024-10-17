NbPhotocopie = int(input("Entrez un nombre de photocopie "))

print(f"Nombre entré : {NbPhotocopie}")

MontantFacture = 0

if NbPhotocopie < 10 :
    MontantFacture = NbPhotocopie * 0.1
elif NbPhotocopie < 30:
    MontantFacture = 10 * 0.1 + (NbPhotocopie - 10) * 20
else:
    MontantFacture = 10 * 0.1 + 20 * 0.09 + (NbPhotocopie - 30) * 0.08

print(f"Montant facture : {MontantFacture}")