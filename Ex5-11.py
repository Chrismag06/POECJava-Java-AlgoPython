import math

Partants = int(input("Nombre de cheveaux partant : "))
Joues = int(input("Nombre de cheveaux jourés : "))

Ordre = math.factorial(Partants) / math.factorial(Partants - Joues) 
Desordre = math.factorial(Partants) / (math.factorial(Joues) * math.factorial(Partants - Joues))

print(f"Dans l’ordre : une chance sur {Ordre} de gagner")
print(f"Dans le désordre : une chance sur {Desordre} de gagner")



