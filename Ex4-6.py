ScoreCandidat1 = int(input("Entrez score Candidat1: "))
ScoreCandidat2 = int(input("Entrez score Candidat2: "))
ScoreCandidat3 = int(input("Entrez score Candidat3: "))
ScoreCandidat4 = int(input("Entrez score Candidat4: "))

if ScoreCandidat1 > 50:
    print("Candidat un élu")
elif ScoreCandidat1 < 12.5:
    print("Candidat 1 battu")
elif ScoreCandidat1 < ScoreCandidat2:
    print("Candidat 1  balottage défavorable")
elif ScoreCandidat1 < ScoreCandidat3:
    print("Candidat 1 balottage défavorable")
elif ScoreCandidat1 < ScoreCandidat4:
    print("Candidat 1 balottage défavorable")
else: 
    print("Candidat 1 balottage favorable")