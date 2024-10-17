Nombre = 0

while Nombre < 10 or Nombre > 20:
    Nombre = int(input("Entrez un nombre entre 10 et 20:"))
    match Nombre:
        case  Nombre if Nombre < 10:
            print("Plus grand!")
        case Nombre if Nombre > 20:
            print("Plus petit!")
        case _:
            print("C'est bon c'est dans l'intervalle")