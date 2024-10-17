
Partants = int(input("Nombre de cheveaux partant : "))
Joues = int(input("Nombre de cheveaux jourés : "))

PartantJoue = Partants - Joues

facPartant = 1
facJoue = 1
facPartantJoue = 1

for i in range(1,Partants + 1):
    facPartant *= i

for i in range(1,Joues + 1):
    facJoue *= i

for i in range(1,PartantJoue + 1):
    facPartantJoue *= i

Ordre = facPartant / facPartantJoue 
Desordre = facPartant / (facJoue * facPartantJoue)

print(f"Dans l’ordre : une chance sur {Ordre} de gagner")
print(f"Dans le désordre : une chance sur {Desordre} de gagner")
