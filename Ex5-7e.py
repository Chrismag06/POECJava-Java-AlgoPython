Nombre = int(input("Entrez un nombre : "))

Total = 1

for cpt in range(Nombre,0,-1):
    print(f" {cpt} ", end = " ")
    if cpt > 1:
        print("x", end = " ")       
    Total *= cpt

print("=", end = " ")
print(Total)