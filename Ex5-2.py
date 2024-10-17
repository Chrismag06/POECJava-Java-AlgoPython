
Nombre = 0

while Nombre < 10 or Nombre > 20:
    Nombre = int(input("Entrez un nombre entre 10 et 20:"))
    if Nombre < 10:
        print("Plus grand!")
    else:
        if Nombre > 20:
            print("Plus petit!")
        else:
            print("C'est bon c'est dans l'intervalle")
            