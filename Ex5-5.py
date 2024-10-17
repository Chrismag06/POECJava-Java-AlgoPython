Nombre = int(input("Entrez un nombre : "))

print(f"table de {Nombre} : ")

for cpt in range(1,11):
    print(f"{Nombre} X {cpt} = {Nombre * cpt}")