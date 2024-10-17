Nombres = []

for i in range(1,21):
    Nombres.append(int(input(f"Entrez un nombre  {i}: ")))

NombreMax = 0

for i in range(0,len(Nombres)):
    if NombreMax < Nombres[i]:
        NombreMax = Nombres[i]

print(f"Le nombre max est {NombreMax}")

