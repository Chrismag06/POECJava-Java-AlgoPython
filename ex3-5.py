print("Entrez deux nombres : ") 

m = int(input("Entrez nombres un: "))
n = int(input("Entrez nombres deux: "))

if m == 0 or n == 0:
  print( "Le produit est nul")
elif (m < 0 and n < 0) or (m > 0 and n > 0):
  print("Le produit est positif")
else:
  print("Le produit est négatif")
