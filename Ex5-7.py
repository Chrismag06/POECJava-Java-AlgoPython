import math

Nombre = int(input("Entrez un nombre : "))

Total = f"{Nombre}! = "

for cpt in range(1,Nombre):
    Total += f"{cpt} x " 

Total =  Total[:-2]

Total +=  "= " + str(math.factorial(Nombre))

print(Total)