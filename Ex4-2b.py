import datetime 

heure = int(input("Entrez une heure "))
minute = int(input("Entrez une minute "))

print(f"l'heure est {heure}:{minute}")

minute += 1

if minute > 59:
    minute = 0
    heure += 1

if heure > 23: 
    heure = 0

print(f"l'heure modifié est {heure:02d}:{minute:02d}   ")

