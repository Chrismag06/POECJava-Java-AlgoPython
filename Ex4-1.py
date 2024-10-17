Tutu = int(input("Entrez une première variable décimale "))
Tata = input("Entrez une deuxième variable texte ")
Toto = int(input("Entrez une troisième variable décimale "))

#if Tutu > Toto + 4 or Tata == "OK":
if Tutu < Toto + 4 and Tata != "OK":
  Tutu = Tutu + 1
else:
  Tutu = Tutu + 1

print(f"tutu : {Tutu} - Toto : {Toto} - Tata : {Tata}")
