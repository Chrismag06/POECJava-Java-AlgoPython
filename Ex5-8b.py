PlusGrand = 0
for i in range(1,21):
    Nombre = int(input(f"Entrez un nombre  {i}: "))
    if PlusGrand < Nombre:
        PlusGrand = Nombre

print(f"Le plus grand nombre est {PlusGrand}")

