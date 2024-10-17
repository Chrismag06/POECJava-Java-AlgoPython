Nombres = []

for i in range(1,21):
    Nombres.append(int(input(f"Entrez un nombre  {i}: ")))

Nombres.sort()

print(f"Le plus grand nombre est {Nombres[-1:]}")