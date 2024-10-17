
ScoreCandidat = []

ScoreCandidat.append(f"{int(input("Entrez score Candidat1: ")):02d}_Cand1")
ScoreCandidat.append(f"{int(input("Entrez score Candidat2: ")):02d}_Cand2")
ScoreCandidat.append(f"{int(input("Entrez score Candidat3: ")):02d}_Cand3")
ScoreCandidat.append(f"{int(input("Entrez score Candidat4: ")):02d}_Cand4")

ScoreCandidat.sort()

print (ScoreCandidat)

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