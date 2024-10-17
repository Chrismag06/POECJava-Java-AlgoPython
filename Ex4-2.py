from datetime import datetime, timedelta

heure = int(input("Entrez une heure "))
minute = int(input("Entrez une minute "))

heures = datetime(2023, 3, 14, heure, minute)

print(f"heure entrée : {heures}") 

heures += timedelta(minutes=1) 

print(f"changed time: {heures.hour}:{heures.minute}")