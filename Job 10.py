def verifier_nombre(nombre):
    if isinstance(nombre, int) and nombre > 0:
        if nombre % 2 == 0:
            print(f"{nombre} est un nombre pair")
        else:
            print(f"{nombre} est un nombre impair")
    else:
        print("Veuillez entrer un nombre entier positif")

