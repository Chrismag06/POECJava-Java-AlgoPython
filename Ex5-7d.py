Nombre = int(input("Entrez un nombre : "))

Total = 1

for cpt in range(1,Nombre + 1):
    print(f" {cpt} ", end = " ")
    if cpt < Nombre:
        print("x", end = " ")
    else:
        print("=", end = " ")
    Total *= cpt

print(Total)
