print("Entrez deux nombres")

m = int(input())
n = int(input())

if (m > 0 and n > 0) or (m < 0 and n < 0):
  print("Leur produit est positif") 
else:
  print("Leur produit est négatif")